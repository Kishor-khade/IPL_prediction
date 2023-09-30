import pandas as pd
import streamlit as st
import pickle

st.title('IPL win predictor')

teams = ['KKR', 'MI', 'RCB', 'LSG', 'RR', 'CSK', 'PBKS', 'DC', 'SRH', 'GT']

venue = ['Wankhede Stadium, Mumbai', 
        'Brabourne Stadium, Mumbai',
        'Dr DY Patil Sports Academy, Navi Mumbai',
        'Maharashtra Cricket Association Stadium, Pune',
        'Eden Gardens, Kolkata',
        'Narendra Modi Stadium, Motera, Ahmedabad',
        'Dubai International Cricket Stadium', 
        'Sharjah Cricket Stadium',
        'Sheikh Zayed Stadium, Abu Dhabi', 
        'Arun Jaitley Stadium, Delhi',
        'MA Chidambaram Stadium, Chepauk, Chennai',
        'Sawai Mansingh Stadium, Jaipur',
        'M.Chinnaswamy Stadium, Bengaluru',
        'Rajiv Gandhi International Stadium, Uppal, Hyderabad',
        'Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh',
        'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam',
        'Holkar Cricket Stadium, Indore',
        'Shaheed Veer Narayan Singh International Stadium, Raipur',
        'Sardar Patel (Gujarat) Stadium, Motera, Ahmedabad',
        'JSCA International Stadium Complex, Ranchi',
        'Barabati Stadium, Cuttack',
        'Himachal Pradesh Cricket Association Stadium, Dharamsala',
        'Dr DY Patil Sports Academy, Mumbai',
        'Vidarbha Cricket Association Stadium, Jamtha, Nagpur',
        'Newlands, Cape Town', 
        "St George's Park, Port Elizabeth",
        'Kingsmead, Durban', 
        'SuperSport Park, Centurion',
        'Buffalo Park, East London', 
        'The Wanderers Stadium, Johannesburg',
        'Diamond Oval, Kimberley', 
        'Mangaung Oval, Bloemfontein']

pipe = pickle.load(open('/pipe.pkl', 'rb'))


col1,col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team', sorted(teams))

teams.remove(batting_team)
with col2:
    bowling_team = st.selectbox('select the bowling team', sorted(teams))
    
    
selected_venue = st.selectbox('Select stadium', sorted(venue))

target = st.number_input('Target')

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Score')
    
with col4:
    overs = st.number_input('Overs completed')
    
with col5:
    wickets = st.number_input('Wickets')
    
if st.button('Predict Probability'):
    runs_left = target-score
    balls_left = 120-(overs*6)
    wickets_left = 10-wickets
    crr = score/overs
    rrr = runs_left*6/balls_left
    
    input_df = pd.DataFrame(
        {
            'batting_team':[batting_team],
            'bowling_team':[bowling_team],
            'venue_name':[selected_venue],
            'runs_left':[runs_left],
            'balls_left':[balls_left],
            'wickets_left':[wickets_left],
            'runs_x':target,
            'current_run_rate':[crr],
            'required_run_rate':[rrr]
        })
    
    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    
    st.header(batting_team+'- '+str(round(win*100))+'%')
    st.header(bowling_team+'- '+str(round(loss*100))+'%')
    
    
    