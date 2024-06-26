def page_1_user_style(main_img):
    return f"""<style>
                @keyframes fadeInDown {{
                     0% {{
                          opacity: 0;
                          transform: translate3d(0, -10%, 0);
                          }}
                     to {{
                          opacity: 1;
                          transform: translateZ(0);
                          }}
                }}
                .main {{
                     background-image: url("data:image/png;base64,{main_img}");
                     background-size:cover;
                     padding:0px;
                }}
                .css-z5fcl4 {{ 
                          padding-left : 10%;
                          padding-right : 10%;
                          padding-top : 2rem;
                          display : flex;  
                }}
                div.row-widget.stRadio > div{{
                     display : flex;
                     justify-content : space-around;
                     align-items: center;
                     flex-basis : 3rem;
                }}
                [role="radiogroup"] {{
                     margin : 0 auto;
                }}
                [data-baseweb="radio"] {{
                     margin : 0;
                }}
                /*
                .st-dr, .st-dt, .st-du, .st-ed{{
                     margin : 0 auto;
                     padding-right :0;
                     padding-left:2px;
                }}
                */
                [data-baseweb="radio"] div {{
                     background-color : #2D5AF0;
                }}
                [data-baseweb="radio"] div>div {{
                     background-color : #FFFFFF;
                }}
                [data-baseweb="radio"] div:nth-child(3) {{
                     visibility:hidden;
                }}
                .st-en, .st-em, .st-el, .st-ek {{
                     border-color : #2D5AF0;
                }}
                .essential_menu{{
                     color : red;
                }}
                .menu_name {{
                     font-size : 20px;
                     padding-top : 0px;
                     font-family : 'Nanumsquare'
                }}
                .css-115gedg {{
                     display : flex;
                     align-content: stretch;
                }}
                .css-vsyxl8{{
                     display : flex;
                     flex-wrap: wrap;
                     align-content: stretch;
                }}
                .main_message {{
                     word-break: keep-all;
                     font-size : 36px;
                     text-align : left;
                     font-weight : bold;
                     padding-top : 14%;
                     font-family : 'Nanumsquare';
                     animation: fadeInDown 1s;
                     padding-left : 8rem;
                     padding-bottom : 1rem;
                }}
                #real_ad {{
                     padding-left : 8rem;
                     padding-bottom : 1rem;
                     box-sizing:content-box;
                }}
                .additional_message {{
                     display : flex;
                     flex-grow : 1;
                     justify-content : start;
                     color : #989898;
                     font-family : 'Nanumsquare';
                }}
                .info_message {{
                     display : flex;
                     flex-grow : 1;
                     justify-content : end;
                     color : #989898;
                     font-family : 'Nanumsquare'
                }}
                .check_message{{
                     word-break: keep-all;
                     font-size : 20px;
                     text-align : left;
                     font-weight : 700;
                     color : red;
                     font-family : 'Nanumsquare';
                     padding-left : 8rem;
                     padding-right : 8rem;
                }}
                [class="row-widget stButton"] {{
                     display : flex;
                     justify-content : start;
                     margin-left : auto;
                     margin-right : auto;

                }}
                [class="row-widget stButton"] button {{
                     border : none;
                     padding-left : 8rem;
                     background-color: transparent;
                }}
                [class="row-widget stButton"] button:hover {{
                     background-color: transparent;
                }}
                [class="row-widget stButton"] button>div {{
                     display : flex;
                     border-radius: 50px;
                     background : #D9D9D9;
                     filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
                     width : 9em;
                     height : 2.5em;
                     font-size : 40px;
                     justify-content : center;
                     font-family : 'Nanumsquare';
                }}
                [class="row-widget stButton"] button>div:hover{{
                     transform : scale(1.1);
                     background : #2D5AF0;
                     transition : .5s;
                }}
                [class="row-widget stButton"] button>div>p {{
                     font-size : 40px;
                     font-weight: 700;
                     color: #FFFFFF;
                     text-align: center;
                     margin : auto;
                }}
                [data-testid="stHorizontalBlock"] {{
                     justify-content : space-around;
                     flex-direction: row;
                     flex-wrap : wrap;
                }}
                /* 샘플이력서 이름 구간 */
                [data-testid="stVerticalBlock"] > div:nth-child(9){{
                     gap:0;
                }}
                [class="row-widget stDownloadButton"] {{
                     display : inline-flex;
                     justify-content : flex-start;
                     margin-left : 0;
                     margin-right : 0;
                     flex-shrink : 1;
                }}
                [class="row-widget stDownloadButton"] button{{
                     padding : 0;
                     border : none;
                     max-width : 100%;
                     flex-grow : 0;
                     align-items: center;
                }}
                [class="row-widget stDownloadButton"] button>div:hover{{
                     font-weight : 700;
                     transform : scale(1.1);
                     transition : .5s;
                }}
                [class="row-widget stDownloadButton"] button:active{{
                     background-color : transparent;
                }}
                [class="row-widget stDownloadButton"] button>div>p {{
                     font-size : 15px;
                     font-family : 'Nanumsquare';
                     text-align : left;
                }}
                .interviewer_icon{{
                     display : flex;
                     flex-direction : row;
                     justify-content : space-between;
                }}
                #persona {{
                     display : flex;
                     justify-content : center;
                     align-content : center;
                     flex-direction : column;
                }}
                #persona figcaption {{
                     font-family : 'Nanumsquare';
                     font-size : 14px;
                     color : #989898;
                     text-align : center;
                }}
                #persona img {{
                     align-self : center;
                     max-width : 100%;
                     height : auto;
                     flex-shrink : 1;
                     filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));
                     margin : 0;
                }}
                #persona p {{
                     margin-bottom : -1rem;
                     text-align : center;
                     font-style: normal;
                     font-size : 17px;
                     font-weight : 500;
                     font-family : 'Nanumsquare';
                }}
                /* 결과 샘플 */
                [data-testid="stHorizontalBlock"] > div:nth-child(2) > div > div> div:nth-child(4) > div {{
                     padding-left : 8rem;
                     max-width : 80%;
                     justify-content: flex-start;
                }}
                [data-testid="stExpander"] {{
                     padding-left : 7rem;
                     max-width : 70%;
                }}
                [data-baseweb="accordion"] {{
                     border : none;
                }}
                [data-baseweb="accordion"] >li >div >svg {{
                     visibility : hidden;
                }}


                </style>"""
