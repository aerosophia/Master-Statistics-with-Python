{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red164\green191\blue255;\red23\green23\blue23;\red255\green255\blue255;
\red252\green115\blue96;\red117\green255\blue242;\red129\green131\blue134;\red254\green219\blue112;}
{\*\expandedcolortbl;;\cssrgb\c70196\c80000\c100000;\cssrgb\c11765\c11765\c11765;\cssrgb\c100000\c100000\c100000;
\cssrgb\c100000\c53725\c45098;\cssrgb\c51373\c100000\c96078;\cssrgb\c57647\c58431\c59608;\cssrgb\c100000\c87843\c51373;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl480\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 matplotlib\cf4 \strokec4 .\cf6 \strokec6 pyplot\cf4 \strokec4  \cf2 \strokec2 as\cf4 \strokec4  \cf5 \strokec5 plt\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 pandas\cf4 \strokec4  \cf2 \strokec2 as\cf4 \strokec4  \cf5 \strokec5 pd\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 seaborn\cf4 \strokec4  \cf2 \strokec2 as\cf4 \strokec4  \cf5 \strokec5 sns\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 codecademylib3\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf7 \cb3 \strokec7 # load in the data\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 df\cf4 \strokec4  = \cf5 \strokec5 pd\cf4 \strokec4 .\cf6 \strokec6 read_csv\cf4 \strokec4 (\cf8 \strokec8 "mushroom_data.csv"\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 df\cf4 \strokec4 .\cf6 \strokec6 head\cf4 \strokec4 ())\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf7 \cb3 \strokec7 # list of all column headers \cf4 \cb1 \strokec4 \
\cf7 \cb3 \strokec7 #columns = df.columns.tolist()\cf4 \cb1 \strokec4 \
\
\cf7 \cb3 \strokec7 #we can iterate df.columns\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb3 \strokec2 for\cf4 \strokec4  \cf5 \strokec5 i\cf4 \strokec4  \cf2 \strokec2 in\cf4 \strokec4  \cf5 \strokec5 df\cf4 \strokec4 .\cf6 \strokec6 columns\cf4 \strokec4 :\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3   \cf7 \strokec7 #print(i)\cf4 \cb1 \strokec4 \
\cb3   \cf7 \strokec7 #plotting your data for each column\cf4 \cb1 \strokec4 \
\cb3   \cf5 \strokec5 sns\cf4 \strokec4 .\cf6 \strokec6 countplot\cf4 \strokec4 (\cf5 \strokec5 df\cf4 \strokec4 [\cf5 \strokec5 i\cf4 \strokec4 ],\cf5 \strokec5 order\cf4 \strokec4 =\cf5 \strokec5 df\cf4 \strokec4 [\cf5 \strokec5 i\cf4 \strokec4 ].\cf6 \strokec6 value_counts\cf4 \strokec4 ().\cf6 \strokec6 index\cf4 \strokec4 )\cb1 \
\cb3   \cf7 \strokec7 # rotates the value labels slightly so they don\'92t overlap, also slightly increases font size\cf4 \cb1 \strokec4 \
\cb3   \cf5 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 xticks\cf4 \strokec4 (\cf5 \strokec5 rotation\cf4 \strokec4 =\cf5 \strokec5 30\cf4 \strokec4 , \cf5 \strokec5 fontsize\cf4 \strokec4 =\cf5 \strokec5 10\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf7 \cb3 \strokec7 # increases the variable label font size slightly to increase readability\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3   \cf5 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 xlabel\cf4 \strokec4 (\cf5 \strokec5 i\cf4 \strokec4 , \cf5 \strokec5 fontsize\cf4 \strokec4 =\cf5 \strokec5 12\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf7 \cb3 \strokec7 #adding a title\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3   \cf5 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 title\cf4 \strokec4 (\cf5 \strokec5 i\cf4 \strokec4  + \cf8 \strokec8 " Value Counts"\cf4 \strokec4 )\cb1 \
\cb3   \cb1 \
\cb3   \cf5 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 show\cf4 \strokec4 ()\cb1 \
\cb3   \cf5 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 clf\cf4 \strokec4 ()\cb1 \
\
\
\
\
\
\
\
\
\
\
\
}