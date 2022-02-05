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
\outl0\strokewidth0 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 codecademylib3\cf4 \cb1 \strokec4 \
\
\cf6 \cb3 \strokec6 # Import pandas with alias\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 pandas\cf4 \strokec4  \cf2 \strokec2 as\cf4 \strokec4  \cf5 \strokec5 pd\cf4 \cb1 \strokec4 \
\
\cf6 \cb3 \strokec6 # Read in the census dataframe\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 census\cf4 \strokec4  = \cf5 \strokec5 pd\cf4 \strokec4 .\cf7 \strokec7 read_csv\cf4 \strokec4 (\cf8 \strokec8 'census_data.csv'\cf4 \strokec4 , \cf5 \strokec5 index_col\cf4 \strokec4 =\cf5 \strokec5 0\cf4 \strokec4 )\cb1 \
\
\cf6 \cb3 \strokec6 #Viewing the first five rows \cf4 \cb1 \strokec4 \
\cb3 print(\cf5 \strokec5 census\cf4 \strokec4 .\cf7 \strokec7 head\cf4 \strokec4 ())\cb1 \
\
\cf6 \cb3 \strokec6 #Data types of each variable\cf4 \cb1 \strokec4 \
\cb3 print(\cf5 \strokec5 census\cf4 \strokec4 .\cf7 \strokec7 dtypes\cf4 \strokec4 )\cb1 \
\
\cf6 \cb3 \strokec6 # Compare the Data Types and the Dataframe description, 'birth-year' has been assigned the str type whereas it should be in int. Let's alter it.\cf4 \cb1 \strokec4 \
\
\cf6 \cb3 \strokec6 # let's print the unique values of the variable 'birth_year'\cf4 \cb1 \strokec4 \
\cb3 print(\cf5 \strokec5 census\cf4 \strokec4 [\cf8 \strokec8 'birth_year'\cf4 \strokec4 ].\cf7 \strokec7 unique\cf4 \strokec4 ())\cb1 \
\
\cf6 \cb3 \strokec6 # Altering Data: Replacing the missing value\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 census\cf4 \strokec4 [\cf8 \strokec8 'birth_year'\cf4 \strokec4 ]=\cf5 \strokec5 census\cf4 \strokec4 [\cf8 \strokec8 'birth_year'\cf4 \strokec4 ].\cf7 \strokec7 replace\cf4 \strokec4 ([\cf8 \strokec8 'missing'\cf4 \strokec4 ], \cf5 \strokec5 1967\cf4 \strokec4 )\cb1 \
\
\cf6 \cb3 \strokec6 #Checking if the replacement has been done\cf4 \cb1 \strokec4 \
\cb3 print(\cf5 \strokec5 census\cf4 \strokec4 [\cf8 \strokec8 'birth_year'\cf4 \strokec4 ].\cf7 \strokec7 unique\cf4 \strokec4 ())\cb1 \
\
\cf6 \cb3 \strokec6 #changing the datatypes\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 census\cf4 \strokec4 [\cf8 \strokec8 'birth_year'\cf4 \strokec4 ]=\cf5 \strokec5 census\cf4 \strokec4 [\cf8 \strokec8 'birth_year'\cf4 \strokec4 ].\cf7 \strokec7 astype\cf4 \strokec4 (int)\cb1 \
\
\cf6 \cb3 \strokec6 #printing the data types to check\cf4 \cb1 \strokec4 \
\cb3 print(\cf5 \strokec5 census\cf4 \strokec4 .\cf7 \strokec7 dtypes\cf4 \strokec4 )\cb1 \
\
\cf6 \cb3 \strokec6 #Calculating the average birth year\cf4 \cb1 \strokec4 \
\cb3 print(\cf5 \strokec5 census\cf4 \strokec4 [\cf8 \strokec8 'birth_year'\cf4 \strokec4 ].\cf7 \strokec7 mean\cf4 \strokec4 ())\cb1 \
\
\cf6 \cb3 \strokec6 #Setting an order to 'higher_tax'\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 census\cf4 \strokec4 [\cf8 \strokec8 'higher_tax'\cf4 \strokec4 ] = \cf5 \strokec5 pd\cf4 \strokec4 .\cf7 \strokec7 Categorical\cf4 \strokec4 (\cf5 \strokec5 census\cf4 \strokec4 [\cf8 \strokec8 'higher_tax'\cf4 \strokec4 ],[\cf8 \strokec8 'strongly'\cf4 \strokec4 , \cf8 \strokec8 'disagree'\cf4 \strokec4 , \cf8 \strokec8 'neutral'\cf4 \strokec4 , \cf8 \strokec8 'agree'\cf4 \strokec4 , \cf8 \strokec8 'strongly agree'\cf4 \strokec4 ], \cf5 \strokec5 ordered\cf4 \strokec4 =\cf2 \strokec2 True\cf4 \strokec4 )\cb1 \
\
\cf6 \cb3 \strokec6 #Print out unique values of 'higher_tax'\cf4 \cb1 \strokec4 \
\cb3 print(\cf5 \strokec5 census\cf4 \strokec4 [\cf8 \strokec8 'higher_tax'\cf4 \strokec4 ].\cf7 \strokec7 unique\cf4 \strokec4 ())\cb1 \
\
\cf6 \cb3 \strokec6 #Label encode 'higher_tax'\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 census\cf4 \strokec4 [\cf8 \strokec8 'higher_tax'\cf4 \strokec4 ] = \cf5 \strokec5 census\cf4 \strokec4 [\cf8 \strokec8 'higher_tax'\cf4 \strokec4 ].\cf7 \strokec7 cat\cf5 \strokec5 .\cf7 \strokec7 codes\cf4 \cb1 \strokec4 \
\
\cf6 \cb3 \strokec6 #The median of 'higher_tax'\cf4 \cb1 \strokec4 \
\cb3 print(\cf5 \strokec5 census\cf4 \strokec4 [\cf8 \strokec8 'higher_tax'\cf4 \strokec4 ].\cf7 \strokec7 median\cf4 \strokec4 ())\cb1 \
\
\
\cf6 \cb3 \strokec6 #One-Hot Encode 'marital_status' (P.D: OHE are useful in machine learning techniques!)\cf4 \cb1 \strokec4 \
\
\cf5 \cb3 \strokec5 census\cf4 \strokec4  = \cf5 \strokec5 pd\cf4 \strokec4 .\cf7 \strokec7 get_dummies\cf4 \strokec4 (\cf5 \strokec5 census\cf4 \strokec4 , \cf5 \strokec5 columns\cf4 \strokec4 =[\cf8 \strokec8 'marital_status'\cf4 \strokec4 ])\cb1 \
\cb3 print(\cf5 \strokec5 census\cf4 \strokec4 .\cf7 \strokec7 head\cf4 \strokec4 ())\cb1 \
\
\
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \
}