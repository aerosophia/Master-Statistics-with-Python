{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red164\green191\blue255;\red23\green23\blue23;\red255\green255\blue255;
\red252\green115\blue96;\red117\green255\blue242;\red254\green219\blue112;}
{\*\expandedcolortbl;;\cssrgb\c70196\c80000\c100000;\cssrgb\c11765\c11765\c11765;\cssrgb\c100000\c100000\c100000;
\cssrgb\c100000\c53725\c45098;\cssrgb\c51373\c100000\c96078;\cssrgb\c100000\c87843\c51373;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl480\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 codecademylib3_seaborn\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 pandas\cf4 \strokec4  \cf2 \strokec2 as\cf4 \strokec4  \cf5 \strokec5 pd\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 from\cf4 \strokec4  \cf5 \strokec5 matplotlib\cf4 \strokec4  \cf2 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 pyplot\cf4 \strokec4  \cf2 \strokec2 as\cf4 \strokec4  \cf5 \strokec5 plt\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 healthcare\cf4 \strokec4  = \cf5 \strokec5 pd\cf4 \strokec4 .\cf6 \strokec6 read_csv\cf4 \strokec4 (\cf7 \strokec7 "healthcare.csv"\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 healthcare\cf4 \strokec4 .\cf6 \strokec6 head\cf4 \strokec4 ())\cb1 \
\cb3 print(\cf5 \strokec5 healthcare\cf4 \strokec4 [\cf7 \strokec7 "DRG Definition"\cf4 \strokec4 ].\cf6 \strokec6 unique\cf4 \strokec4 ())\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 chest_pain\cf4 \strokec4  = \cf5 \strokec5 healthcare\cf4 \strokec4 [\cf5 \strokec5 healthcare\cf4 \strokec4 [\cf7 \strokec7 'DRG Definition'\cf4 \strokec4 ] == \cf7 \strokec7 '313 - CHEST PAIN'\cf4 \strokec4 ]\cb1 \
\
\cf5 \cb3 \strokec5 newjersey_chest_pain\cf4 \strokec4  = \cf5 \strokec5 chest_pain\cf4 \strokec4 [\cf5 \strokec5 chest_pain\cf4 \strokec4 [\cf7 \strokec7 'Provider State'\cf4 \strokec4 ] == \cf7 \strokec7 "NJ"\cf4 \strokec4 ]\cb1 \
\
\cf5 \cb3 \strokec5 costs\cf4 \strokec4  = \cf5 \strokec5 newjersey_chest_pain\cf4 \strokec4 [\cf7 \strokec7 ' Average Covered Charges '\cf4 \strokec4 ].\cf6 \strokec6 values\cf4 \cb1 \strokec4 \
\
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 boxplot\cf4 \strokec4 (\cf5 \strokec5 costs\cf4 \strokec4 )\cb1 \
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 show\cf4 \strokec4 ()\cb1 \
\
\cf5 \cb3 \strokec5 states\cf4 \strokec4  = \cf5 \strokec5 chest_pain\cf4 \strokec4 [\cf7 \strokec7 "Provider State"\cf4 \strokec4 ].\cf6 \strokec6 unique\cf4 \strokec4 ()\cb1 \
\
\cf5 \cb3 \strokec5 datasets\cf4 \strokec4 =[]\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb3 \strokec2 for\cf4 \strokec4  \cf5 \strokec5 state\cf4 \strokec4  \cf2 \strokec2 in\cf4 \strokec4  \cf5 \strokec5 states\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3   \cf5 \strokec5 datasets\cf4 \strokec4 .\cf6 \strokec6 append\cf4 \strokec4 (\cf5 \strokec5 chest_pain\cf4 \strokec4 [\cf5 \strokec5 chest_pain\cf4 \strokec4 [\cf7 \strokec7 'Provider State'\cf4 \strokec4 ] == \cf5 \strokec5 state\cf4 \strokec4 ][\cf7 \strokec7 ' Average Covered Charges '\cf4 \strokec4 ].\cf6 \strokec6 values\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 figure\cf4 \strokec4 (\cf5 \strokec5 figsize\cf4 \strokec4 =(\cf5 \strokec5 20\cf4 \strokec4 ,\cf5 \strokec5 6\cf4 \strokec4 ))\cb1 \
\
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 boxplot\cf4 \strokec4 (\cf5 \strokec5 datasets\cf4 \strokec4 ,\cf5 \strokec5 labels\cf4 \strokec4 =\cf5 \strokec5 states\cf4 \strokec4 )\cb1 \
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 show\cf4 \strokec4 ()\cb1 \
\
}