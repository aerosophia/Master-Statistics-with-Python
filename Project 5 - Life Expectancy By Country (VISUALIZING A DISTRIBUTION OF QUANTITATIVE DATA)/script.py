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
\outl0\strokewidth0 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 codecademylib3_seaborn\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 numpy\cf4 \strokec4  \cf2 \strokec2 as\cf4 \strokec4  \cf5 \strokec5 np\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 pandas\cf4 \strokec4  \cf2 \strokec2 as\cf4 \strokec4  \cf5 \strokec5 pd\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 matplotlib\cf4 \strokec4 .\cf6 \strokec6 pyplot\cf4 \strokec4  \cf2 \strokec2 as\cf4 \strokec4  \cf5 \strokec5 plt\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 data\cf4 \strokec4  = \cf5 \strokec5 pd\cf4 \strokec4 .\cf6 \strokec6 read_csv\cf4 \strokec4 (\cf7 \strokec7 "country_data.csv"\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 data\cf4 \strokec4 .\cf6 \strokec6 head\cf4 \strokec4 ())\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf8 \cb3 \strokec8 #Getting one single column from a Panda DataFrame\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 life_expectancy\cf4 \strokec4  = \cf5 \strokec5 data\cf4 \strokec4 [\cf7 \strokec7 "Life Expectancy"\cf4 \strokec4 ]\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf8 \cb3 \strokec8 #Quartiles of life_expectancy\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 life_expectancy_quartiles\cf4 \strokec4  =\cf5 \strokec5 np\cf4 \strokec4 .\cf6 \strokec6 quantile\cf4 \strokec4 (\cf5 \strokec5 life_expectancy\cf4 \strokec4 , [\cf5 \strokec5 0.25\cf4 \strokec4 ,\cf5 \strokec5 0.5\cf4 \strokec4 ,\cf5 \strokec5 0.75\cf4 \strokec4 ])\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 life_expectancy_quartiles\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf8 \cb3 \strokec8 #Plotting histogram of life_expectancy\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8 #plt.hist(life_expectancy)\cf4 \cb1 \strokec4 \
\cf8 \cb3 \strokec8 #plt.show()\cf4 \cb1 \strokec4 \
\
\cf8 \cb3 \strokec8 #Getting one single column from a Panda DataFrame\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 gdp\cf4 \strokec4  = \cf5 \strokec5 data\cf4 \strokec4 [\cf7 \strokec7 "GDP"\cf4 \strokec4 ]\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf8 \cb3 \strokec8 #MEDIAN GDP\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 median_gdp\cf4 \strokec4  = \cf5 \strokec5 np\cf4 \strokec4 .\cf6 \strokec6 quantile\cf4 \strokec4 (\cf5 \strokec5 gdp\cf4 \strokec4 ,\cf5 \strokec5 0.5\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf8 \cb3 \strokec8 #Selecting the rows referring to low GDP and the rows referring to high GDP\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 low_gdp\cf4 \strokec4  = \cf5 \strokec5 data\cf4 \strokec4 [\cf5 \strokec5 data\cf4 \strokec4 [\cf7 \strokec7 'GDP'\cf4 \strokec4 ] \cf5 \strokec5 <\cf4 \strokec4 = \cf5 \strokec5 median_gdp\cf4 \strokec4 ]\cb1 \
\cf5 \cb3 \strokec5 high_gdp\cf4 \strokec4  = \cf5 \strokec5 data\cf4 \strokec4 [\cf5 \strokec5 data\cf4 \strokec4 [\cf7 \strokec7 'GDP'\cf4 \strokec4 ] \cf5 \strokec5 >\cf4 \strokec4  \cf5 \strokec5 median_gdp\cf4 \strokec4 ]\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf8 \cb3 \strokec8 #Printing the quartiles of these data sets\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 low_gdp_quartiles\cf4 \strokec4  = \cf5 \strokec5 np\cf4 \strokec4 .\cf6 \strokec6 quantile\cf4 \strokec4 (\cf5 \strokec5 low_gdp\cf4 \strokec4 [\cf7 \strokec7 "Life Expectancy"\cf4 \strokec4 ],[\cf5 \strokec5 0.25\cf4 \strokec4 ,\cf5 \strokec5 0.5\cf4 \strokec4 ,\cf5 \strokec5 0.75\cf4 \strokec4 ])\cb1 \
\cf5 \cb3 \strokec5 high_gdp_quartiles\cf4 \strokec4  = \cf5 \strokec5 np\cf4 \strokec4 .\cf6 \strokec6 quantile\cf4 \strokec4 (\cf5 \strokec5 high_gdp\cf4 \strokec4 [\cf7 \strokec7 "Life Expectancy"\cf4 \strokec4 ],[\cf5 \strokec5 0.25\cf4 \strokec4 ,\cf5 \strokec5 0.5\cf4 \strokec4 ,\cf5 \strokec5 0.75\cf4 \strokec4 ])\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 low_gdp_quartiles\cf4 \strokec4 )\cb1 \
\cb3 print(\cf5 \strokec5 high_gdp_quartiles\cf4 \strokec4 )\cb1 \
\
\
\pard\pardeftab720\sl480\partightenfactor0
\cf8 \cb3 \strokec8 #Plotting histograms\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 hist\cf4 \strokec4 (\cf5 \strokec5 high_gdp\cf4 \strokec4 [\cf7 \strokec7 "Life Expectancy"\cf4 \strokec4 ], \cf5 \strokec5 alpha\cf4 \strokec4  = \cf5 \strokec5 0.5\cf4 \strokec4 , \cf5 \strokec5 label\cf4 \strokec4  = \cf7 \strokec7 "High GDP"\cf4 \strokec4 )\cb1 \
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 hist\cf4 \strokec4 (\cf5 \strokec5 low_gdp\cf4 \strokec4 [\cf7 \strokec7 "Life Expectancy"\cf4 \strokec4 ], \cf5 \strokec5 alpha\cf4 \strokec4  = \cf5 \strokec5 0.5\cf4 \strokec4 , \cf5 \strokec5 label\cf4 \strokec4  = \cf7 \strokec7 "Low GDP"\cf4 \strokec4 )\cb1 \
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 legend\cf4 \strokec4 ()\cb1 \
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 show\cf4 \strokec4 ()\cb1 \
}