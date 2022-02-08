{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red164\green191\blue255;\red23\green23\blue23;\red255\green255\blue255;
\red252\green115\blue96;\red117\green255\blue242;\red254\green219\blue112;\red129\green131\blue134;}
{\*\expandedcolortbl;;\cssrgb\c70196\c80000\c100000;\cssrgb\c11765\c11765\c11765;\cssrgb\c100000\c100000\c100000;
\cssrgb\c100000\c53725\c45098;\cssrgb\c51373\c100000\c96078;\cssrgb\c100000\c87843\c51373;\cssrgb\c57647\c58431\c59608;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl480\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 pandas\cf4 \strokec4  \cf2 \strokec2 as\cf4 \strokec4  \cf5 \strokec5 pd\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 numpy\cf4 \strokec4  \cf2 \strokec2 as\cf4 \strokec4  \cf5 \strokec5 np\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 car_eval\cf4 \strokec4  = \cf5 \strokec5 pd\cf4 \strokec4 .\cf6 \strokec6 read_csv\cf4 \strokec4 (\cf7 \strokec7 'car_eval_dataset.csv'\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 car_eval\cf4 \strokec4 .\cf6 \strokec6 head\cf4 \strokec4 ())\cb1 \
\
\
\pard\pardeftab720\sl480\partightenfactor0
\cf8 \cb3 \strokec8 #Table of frequencies of country_manufacturers all the cars \cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 manufacturer_country_freq\cf4 \strokec4  = \cf5 \strokec5 car_eval\cf4 \strokec4 .\cf6 \strokec6 manufacturer_country\cf5 \strokec5 .\cf6 \strokec6 value_counts\cf4 \strokec4 ()\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 manufacturer_country_freq\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf8 \cb3 \strokec8 #The model in this set is 'Japan' with 228 observations\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8 #We can also print the n-th country in this set:\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 manufacturer_country_freq\cf4 \strokec4 .\cf6 \strokec6 index\cf4 \strokec4 [\cf5 \strokec5 4-1\cf4 \strokec4 ])\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf8 \cb3 \strokec8 #Table of proportions of country_manufactuers \cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 manufacturer_country_prop\cf4 \strokec4  = \cf5 \strokec5 car_eval\cf4 \strokec4 .\cf6 \strokec6 manufacturer_country\cf5 \strokec5 .\cf6 \strokec6 value_counts\cf4 \strokec4 (\cf5 \strokec5 normalize\cf4 \strokec4 =\cf2 \strokec2 True\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 manufacturer_country_prop\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf8 \cb3 \strokec8 # 22,8% are manufactured in Japan\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 buying_cost_unique_values\cf4 \strokec4 =\cf5 \strokec5 car_eval\cf4 \strokec4 .\cf6 \strokec6 buying_cost\cf5 \strokec5 .\cf6 \strokec6 unique\cf4 \strokec4 ()\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 buying_cost_unique_values\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 buying_cost_categories\cf4 \strokec4 = [\cf7 \strokec7 'low'\cf4 \strokec4 ,\cf7 \strokec7 'med'\cf4 \strokec4 ,\cf7 \strokec7 'high'\cf4 \strokec4 , \cf7 \strokec7 'vhigh'\cf4 \strokec4 ]\cb1 \
\
\
\
\cf5 \cb3 \strokec5 car_eval\cf4 \strokec4 .\cf6 \strokec6 buying_cost\cf4 \strokec4  = \cf5 \strokec5 pd\cf4 \strokec4 .\cf6 \strokec6 Categorical\cf4 \strokec4 (\cf5 \strokec5 car_eval\cf4 \strokec4 .\cf6 \strokec6 buying_cost\cf4 \strokec4 , \cf5 \strokec5 buying_cost_categories\cf4 \strokec4 , \cf5 \strokec5 ordered\cf4 \strokec4 =\cf2 \strokec2 True\cf4 \strokec4 )\cb1 \
\cf5 \cb3 \strokec5 buying_cost_median\cf4 \strokec4  = \cf5 \strokec5 np\cf4 \strokec4 .\cf6 \strokec6 median\cf4 \strokec4 (\cf5 \strokec5 car_eval\cf4 \strokec4 .\cf6 \strokec6 buying_cost\cf5 \strokec5 .\cf6 \strokec6 cat\cf5 \strokec5 .\cf6 \strokec6 codes\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 buying_cost_categories\cf4 \strokec4 [int(\cf5 \strokec5 buying_cost_median\cf4 \strokec4 )])\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf8 \cb3 \strokec8 #Table of proportions \cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 luggage_prop\cf4 \strokec4  = \cf5 \strokec5 car_eval\cf4 \strokec4 .\cf6 \strokec6 luggage\cf5 \strokec5 .\cf6 \strokec6 value_counts\cf4 \strokec4 (\cf5 \strokec5 dropna\cf4 \strokec4  = \cf2 \strokec2 False\cf4 \strokec4 , \cf5 \strokec5 normalize\cf4 \strokec4 =\cf2 \strokec2 True\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 luggage_prop\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf8 \cb3 \strokec8 #The result is the same if dropna = True, so there are no missing values\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8 #One way to replicate the table of proportions in case of no missing values is:\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 other_prop_table\cf4 \strokec4  = \cf5 \strokec5 car_eval\cf4 \strokec4 .\cf6 \strokec6 luggage\cf5 \strokec5 .\cf6 \strokec6 value_counts\cf4 \strokec4 ()/len(\cf5 \strokec5 car_eval\cf4 \strokec4 .\cf6 \strokec6 luggage\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 other_prop_table\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf8 \cb3 \strokec8 #Both proportion tables are the same! REMEMBER: ONLY WIHTOUT NaN VALUES!!!\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8 #Count(sum) of cars with 5 doors or more\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print((\cf5 \strokec5 car_eval\cf4 \strokec4 .\cf6 \strokec6 doors\cf4 \strokec4  == \cf7 \strokec7 '5more'\cf4 \strokec4 ).\cf6 \strokec6 sum\cf4 \strokec4 ())\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf8 \cb3 \strokec8 #to calculate the proportion of cars that have 5+ doors, we can use the mean() function\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 doors_prop\cf4 \strokec4  = \cf5 \strokec5 car_eval\cf4 \strokec4 .\cf6 \strokec6 doors\cf5 \strokec5 .\cf6 \strokec6 value_counts\cf4 \strokec4 (\cf5 \strokec5 normalize\cf4 \strokec4 =\cf2 \strokec2 True\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print((\cf5 \strokec5 car_eval\cf4 \strokec4 .\cf6 \strokec6 doors\cf4 \strokec4  == \cf7 \strokec7 '5more'\cf4 \strokec4 ).\cf6 \strokec6 mean\cf4 \strokec4 ())\cb1 \
\
\
}