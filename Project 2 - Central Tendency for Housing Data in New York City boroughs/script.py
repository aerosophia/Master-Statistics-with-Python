{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red255\green255\blue255;\red129\green131\blue134;\red23\green23\blue23;
\red252\green115\blue96;\red117\green255\blue242;\red164\green191\blue255;\red254\green219\blue112;}
{\*\expandedcolortbl;;\cssrgb\c100000\c100000\c100000;\cssrgb\c57647\c58431\c59608;\cssrgb\c11765\c11765\c11765;
\cssrgb\c100000\c53725\c45098;\cssrgb\c51373\c100000\c96078;\cssrgb\c70196\c80000\c100000;\cssrgb\c100000\c87843\c51373;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl480\partightenfactor0

\f0\fs28 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 \
\
\
\
\pard\pardeftab720\sl480\partightenfactor0
\cf3 \cb4 \strokec3 # Add mean calculations below \cf2 \cb1 \strokec2 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb4 \strokec5 brooklyn_mean\cf2 \strokec2  = \cf5 \strokec5 np\cf2 \strokec2 .\cf6 \strokec6 average\cf2 \strokec2 (\cf5 \strokec5 brooklyn_price\cf2 \strokec2 )\cb1 \
\cf5 \cb4 \strokec5 manhattan_mean\cf2 \strokec2  = \cf5 \strokec5 np\cf2 \strokec2 .\cf6 \strokec6 average\cf2 \strokec2 (\cf5 \strokec5 manhattan_price\cf2 \strokec2 )\cb1 \
\cf5 \cb4 \strokec5 queens_mean\cf2 \strokec2  = \cf5 \strokec5 np\cf2 \strokec2 .\cf6 \strokec6 average\cf2 \strokec2 (\cf5 \strokec5 queens_price\cf2 \strokec2 )\cb1 \
\
\
\pard\pardeftab720\sl480\partightenfactor0
\cf3 \cb4 \strokec3 # Add median calculations below\cf2 \cb1 \strokec2 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb4 \strokec5 brooklyn_median\cf2 \strokec2  = \cf5 \strokec5 np\cf2 \strokec2 .\cf6 \strokec6 median\cf2 \strokec2 (\cf5 \strokec5 brooklyn_price\cf2 \strokec2 )\cb1 \
\cf5 \cb4 \strokec5 manhattan_median\cf2 \strokec2  = \cf5 \strokec5 np\cf2 \strokec2 .\cf6 \strokec6 median\cf2 \strokec2 (\cf5 \strokec5 manhattan_price\cf2 \strokec2 )\cb1 \
\cf5 \cb4 \strokec5 queens_median\cf2 \strokec2  = \cf5 \strokec5 np\cf2 \strokec2 .\cf6 \strokec6 median\cf2 \strokec2 (\cf5 \strokec5 queens_price\cf2 \strokec2 )\cb1 \
\
\
\pard\pardeftab720\sl480\partightenfactor0
\cf3 \cb4 \strokec3 # Add mode calculations below\cf2 \cb1 \strokec2 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb4 \strokec5 brooklyn_mode\cf2 \strokec2  = \cf5 \strokec5 stats\cf2 \strokec2 .\cf6 \strokec6 mode\cf2 \strokec2 (\cf5 \strokec5 brooklyn_price\cf2 \strokec2 )\cb1 \
\cf5 \cb4 \strokec5 manhattan_mode\cf2 \strokec2  = \cf5 \strokec5 stats\cf2 \strokec2 .\cf6 \strokec6 mode\cf2 \strokec2 (\cf5 \strokec5 manhattan_price\cf2 \strokec2 )\cb1 \
\cf5 \cb4 \strokec5 queens_mode\cf2 \strokec2  = \cf5 \strokec5 stats\cf2 \strokec2 .\cf6 \strokec6 mode\cf2 \strokec2 (\cf5 \strokec5 queens_price\cf2 \strokec2 )\cb1 \
\
\
\pard\pardeftab720\sl480\partightenfactor0
\cf3 \cb4 \strokec3 # Mean\cf2 \cb1 \strokec2 \
\pard\pardeftab720\sl480\partightenfactor0
\cf7 \cb4 \strokec7 try\cf2 \strokec2 :\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb4     print(\cf8 \strokec8 "The mean price in Brooklyn is "\cf2 \strokec2  + str(round(\cf5 \strokec5 brooklyn_mean\cf2 \strokec2 , \cf5 \strokec5 2\cf2 \strokec2 )))\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf7 \cb4 \strokec7 except\cf2 \strokec2  \cf5 \strokec5 NameError\cf2 \strokec2 :\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb4     print(\cf8 \strokec8 "The mean price in Brooklyn is not yet defined."\cf2 \strokec2 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf7 \cb4 \strokec7 try\cf2 \strokec2 :\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb4     print(\cf8 \strokec8 "The mean price in Manhattan is "\cf2 \strokec2  + str(round(\cf5 \strokec5 manhattan_mean\cf2 \strokec2 , \cf5 \strokec5 2\cf2 \strokec2 )))\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf7 \cb4 \strokec7 except\cf2 \strokec2  \cf5 \strokec5 NameError\cf2 \strokec2 :\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb4     print(\cf8 \strokec8 "The mean in Manhattan is not yet defined."\cf2 \strokec2 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf7 \cb4 \strokec7 try\cf2 \strokec2 :\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb4     print(\cf8 \strokec8 "The mean price in Queens is "\cf2 \strokec2  + str(round(\cf5 \strokec5 queens_mean\cf2 \strokec2 , \cf5 \strokec5 2\cf2 \strokec2 )))\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf7 \cb4 \strokec7 except\cf2 \strokec2  \cf5 \strokec5 NameError\cf2 \strokec2 :\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb4     print(\cf8 \strokec8 "The mean price in Queens is not yet defined."\cf2 \strokec2 )\cb1 \
\cb4     \cb1 \
\cb4     \cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf3 \cb4 \strokec3 # Median\cf2 \cb1 \strokec2 \
\pard\pardeftab720\sl480\partightenfactor0
\cf7 \cb4 \strokec7 try\cf2 \strokec2 :\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb4     print(\cf8 \strokec8 "The median price in Brooklyn is "\cf2 \strokec2  + str(\cf5 \strokec5 brooklyn_median\cf2 \strokec2 ))\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf7 \cb4 \strokec7 except\cf2 \strokec2  \cf5 \strokec5 NameError\cf2 \strokec2 :\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb4     print(\cf8 \strokec8 "The median price in Brooklyn is not yet defined."\cf2 \strokec2 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf7 \cb4 \strokec7 try\cf2 \strokec2 :\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb4     print(\cf8 \strokec8 "The median price in Manhattan is "\cf2 \strokec2  + str(\cf5 \strokec5 manhattan_median\cf2 \strokec2 ))\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf7 \cb4 \strokec7 except\cf2 \strokec2  \cf5 \strokec5 NameError\cf2 \strokec2 :\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb4     print(\cf8 \strokec8 "The median price in Manhattan is not yet defined."\cf2 \strokec2 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf7 \cb4 \strokec7 try\cf2 \strokec2 :\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb4     print(\cf8 \strokec8 "The median price in Queens is "\cf2 \strokec2  + str(\cf5 \strokec5 queens_median\cf2 \strokec2 ))\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf7 \cb4 \strokec7 except\cf2 \strokec2  \cf5 \strokec5 NameError\cf2 \strokec2 :\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb4     print(\cf8 \strokec8 "The median price in Queens is not yet defined."\cf2 \strokec2 )\cb1 \
\cb4     \cb1 \
\cb4     \cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf3 \cb4 \strokec3 #Mode\cf2 \cb1 \strokec2 \
\pard\pardeftab720\sl480\partightenfactor0
\cf7 \cb4 \strokec7 try\cf2 \strokec2 :\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb4     print(\cf8 \strokec8 "The mode price in Brooklyn is "\cf2 \strokec2  + str(\cf5 \strokec5 brooklyn_mode\cf2 \strokec2 [\cf5 \strokec5 0\cf2 \strokec2 ][\cf5 \strokec5 0\cf2 \strokec2 ]) + \cf8 \strokec8 " and it appears "\cf2 \strokec2  + str(\cf5 \strokec5 brooklyn_mode\cf2 \strokec2 [\cf5 \strokec5 1\cf2 \strokec2 ][\cf5 \strokec5 0\cf2 \strokec2 ]) + \cf8 \strokec8 " times out of "\cf2 \strokec2  + str(len(\cf5 \strokec5 brooklyn_price\cf2 \strokec2 )))\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf7 \cb4 \strokec7 except\cf2 \strokec2  \cf5 \strokec5 NameError\cf2 \strokec2 :\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb4     print(\cf8 \strokec8 "The mode price in Brooklyn is not yet defined."\cf2 \strokec2 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf7 \cb4 \strokec7 try\cf2 \strokec2 :\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb4     print(\cf8 \strokec8 "The mode price in Manhattan is "\cf2 \strokec2  + str(\cf5 \strokec5 manhattan_mode\cf2 \strokec2 [\cf5 \strokec5 0\cf2 \strokec2 ][\cf5 \strokec5 0\cf2 \strokec2 ]) + \cf8 \strokec8 " and it appears "\cf2 \strokec2  + str(\cf5 \strokec5 manhattan_mode\cf2 \strokec2 [\cf5 \strokec5 1\cf2 \strokec2 ][\cf5 \strokec5 0\cf2 \strokec2 ]) + \cf8 \strokec8 " times out of "\cf2 \strokec2  + str(len(\cf5 \strokec5 manhattan_price\cf2 \strokec2 )))\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf7 \cb4 \strokec7 except\cf2 \strokec2  \cf5 \strokec5 NameError\cf2 \strokec2 :\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb4     print(\cf8 \strokec8 "The mode price in Manhattan is not yet defined."\cf2 \strokec2 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf7 \cb4 \strokec7 try\cf2 \strokec2 :\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb4     print(\cf8 \strokec8 "The mode price in Queens is "\cf2 \strokec2  + str(\cf5 \strokec5 queens_mode\cf2 \strokec2 [\cf5 \strokec5 0\cf2 \strokec2 ][\cf5 \strokec5 0\cf2 \strokec2 ]) + \cf8 \strokec8 " and it appears "\cf2 \strokec2  + str(\cf5 \strokec5 queens_mode\cf2 \strokec2 [\cf5 \strokec5 1\cf2 \strokec2 ][\cf5 \strokec5 0\cf2 \strokec2 ]) + \cf8 \strokec8 " times out of "\cf2 \strokec2  + str(len(\cf5 \strokec5 queens_price\cf2 \strokec2 )))\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf7 \cb4 \strokec7 except\cf2 \strokec2  \cf5 \strokec5 NameError\cf2 \strokec2 :\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb4     print(\cf8 \strokec8 "The mode price in Queens is not yet defined."\cf2 \strokec2 )\cb1 \
\
}