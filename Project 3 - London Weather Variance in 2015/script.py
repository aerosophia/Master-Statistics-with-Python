{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red164\green191\blue255;\red23\green23\blue23;\red255\green255\blue255;
\red252\green115\blue96;\red129\green131\blue134;\red117\green255\blue242;\red254\green219\blue112;}
{\*\expandedcolortbl;;\cssrgb\c70196\c80000\c100000;\cssrgb\c11765\c11765\c11765;\cssrgb\c100000\c100000\c100000;
\cssrgb\c100000\c53725\c45098;\cssrgb\c57647\c58431\c59608;\cssrgb\c51373\c100000\c96078;\cssrgb\c100000\c87843\c51373;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl480\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 codecademylib3_seaborn\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 pandas\cf4 \strokec4  \cf2 \strokec2 as\cf4 \strokec4  \cf5 \strokec5 pd\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 numpy\cf4 \strokec4  \cf2 \strokec2 as\cf4 \strokec4  \cf5 \strokec5 np\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 from\cf4 \strokec4  \cf5 \strokec5 weather_data\cf4 \strokec4  \cf2 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 london_data\cf4 \cb1 \strokec4 \
\
\
\pard\pardeftab720\sl480\partightenfactor0
\cf6 \cb3 \strokec6 #Printing: The first five rows of the DataFrame, number of data points, extracting first column from the DF, DF descriptive statistics: mean, variation and standard deviation.\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 london_data\cf4 \strokec4 .\cf7 \strokec7 head\cf4 \strokec4 ())\cb1 \
\cb3 print(len(\cf5 \strokec5 london_data\cf4 \strokec4 ))\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 temp\cf4 \strokec4  = \cf5 \strokec5 london_data\cf4 \strokec4 [\cf8 \strokec8 "TemperatureC"\cf4 \strokec4 ]\cb1 \
\cf5 \cb3 \strokec5 average_temp\cf4 \strokec4  = \cf5 \strokec5 np\cf4 \strokec4 .\cf7 \strokec7 mean\cf4 \strokec4 (\cf5 \strokec5 temp\cf4 \strokec4 )\cb1 \
\
\cf5 \cb3 \strokec5 temperature_var\cf4 \strokec4  = \cf5 \strokec5 np\cf4 \strokec4 .\cf7 \strokec7 var\cf4 \strokec4 (\cf5 \strokec5 temp\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 temperature_var\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 temperature_standard_deviation\cf4 \strokec4  = \cf5 \strokec5 np\cf4 \strokec4 .\cf7 \strokec7 std\cf4 \strokec4 (\cf5 \strokec5 temp\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 temperature_standard_deviation\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf6 \cb3 \strokec6 #Filtering By Month\cf4 \cb1 \strokec4 \
\cf6 \cb3 \strokec6 #For June\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 june\cf4 \strokec4  = \cf5 \strokec5 london_data\cf4 \strokec4 .\cf7 \strokec7 loc\cf4 \strokec4 [\cf5 \strokec5 london_data\cf4 \strokec4 [\cf8 \strokec8 "month"\cf4 \strokec4 ] == \cf5 \strokec5 6\cf4 \strokec4 ][\cf8 \strokec8 "TemperatureC"\cf4 \strokec4 ]\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf6 \cb3 \strokec6 #For July\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 july\cf4 \strokec4  = \cf5 \strokec5 london_data\cf4 \strokec4 .\cf7 \strokec7 loc\cf4 \strokec4 [\cf5 \strokec5 london_data\cf4 \strokec4 [\cf8 \strokec8 "month"\cf4 \strokec4 ] == \cf5 \strokec5 7\cf4 \strokec4 ][\cf8 \strokec8 "TemperatureC"\cf4 \strokec4 ]\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf6 \cb3 \strokec6 #Printing the mean of temperatures in both months\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 np\cf4 \strokec4 .\cf7 \strokec7 mean\cf4 \strokec4 (\cf5 \strokec5 june\cf4 \strokec4 ))\cb1 \
\cb3 print(\cf5 \strokec5 np\cf4 \strokec4 .\cf7 \strokec7 mean\cf4 \strokec4 (\cf5 \strokec5 july\cf4 \strokec4 ))\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf6 \cb3 \strokec6 #Printing the standard deviation of temperatures in both months\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 np\cf4 \strokec4 .\cf7 \strokec7 std\cf4 \strokec4 (\cf5 \strokec5 june\cf4 \strokec4 ))\cb1 \
\cb3 print(\cf5 \strokec5 np\cf4 \strokec4 .\cf7 \strokec7 std\cf4 \strokec4 (\cf5 \strokec5 july\cf4 \strokec4 ))\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf6 \cb3 \strokec6 #The average temperatures and standard deviations are more close in June, higher chance of getting a cooler day! \cf4 \cb1 \strokec4 \
\
\
\cf6 \cb3 \strokec6 #Mean and standard deviation for all month in 2015 and it shows that September is the perfect month to visit London, less variability and temperatures aren't high than average\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb3 \strokec2 for\cf4 \strokec4  \cf5 \strokec5 i\cf4 \strokec4  \cf2 \strokec2 in\cf4 \strokec4  range(\cf5 \strokec5 1\cf4 \strokec4 , \cf5 \strokec5 13\cf4 \strokec4 ):\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3   \cf5 \strokec5 month\cf4 \strokec4  = \cf5 \strokec5 london_data\cf4 \strokec4 .\cf7 \strokec7 loc\cf4 \strokec4 [\cf5 \strokec5 london_data\cf4 \strokec4 [\cf8 \strokec8 "month"\cf4 \strokec4 ] == \cf5 \strokec5 i\cf4 \strokec4 ][\cf8 \strokec8 "TemperatureC"\cf4 \strokec4 ]\cb1 \
\cb3   print(\cf8 \strokec8 "The mean temperature in month "\cf4 \strokec4 +str(\cf5 \strokec5 i\cf4 \strokec4 ) +\cf8 \strokec8 " is "\cf4 \strokec4 + str(\cf5 \strokec5 np\cf4 \strokec4 .\cf7 \strokec7 mean\cf4 \strokec4 (\cf5 \strokec5 month\cf4 \strokec4 )))\cb1 \
\cb3   print(\cf8 \strokec8 "The standard deviation of temperature in month "\cf4 \strokec4 +str(\cf5 \strokec5 i\cf4 \strokec4 ) +\cf8 \strokec8 " is "\cf4 \strokec4 + str(\cf5 \strokec5 np\cf4 \strokec4 .\cf7 \strokec7 std\cf4 \strokec4 (\cf5 \strokec5 month\cf4 \strokec4 )) +\cf8 \strokec8 "\\n"\cf4 \strokec4 )\cb1 \
\
}