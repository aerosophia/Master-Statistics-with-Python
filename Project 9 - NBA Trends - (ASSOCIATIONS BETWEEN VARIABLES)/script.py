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
\outl0\strokewidth0 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 numpy\cf4 \strokec4  \cf2 \strokec2 as\cf4 \strokec4  \cf5 \strokec5 np\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 pandas\cf4 \strokec4  \cf2 \strokec2 as\cf4 \strokec4  \cf5 \strokec5 pd\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 from\cf4 \strokec4  \cf5 \strokec5 scipy\cf4 \strokec4 .\cf6 \strokec6 stats\cf4 \strokec4  \cf2 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 pearsonr\cf4 \strokec4 , \cf5 \strokec5 chi2_contingency\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 matplotlib\cf4 \strokec4 .\cf6 \strokec6 pyplot\cf4 \strokec4  \cf2 \strokec2 as\cf4 \strokec4  \cf5 \strokec5 plt\cf4 \cb1 \strokec4 \
\cf2 \cb3 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 seaborn\cf4 \strokec4  \cf2 \strokec2 as\cf4 \strokec4  \cf5 \strokec5 sns\cf4 \cb1 \strokec4 \
\
\cf2 \cb3 \strokec2 import\cf4 \strokec4  \cf5 \strokec5 codecademylib3\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 np\cf4 \strokec4 .\cf6 \strokec6 set_printoptions\cf4 \strokec4 (\cf5 \strokec5 suppress\cf4 \strokec4 =\cf2 \strokec2 True\cf4 \strokec4 , \cf5 \strokec5 precision\cf4 \strokec4  = \cf5 \strokec5 2\cf4 \strokec4 )\cb1 \
\
\cf5 \cb3 \strokec5 nba\cf4 \strokec4  = \cf5 \strokec5 pd\cf4 \strokec4 .\cf6 \strokec6 read_csv\cf4 \strokec4 (\cf7 \strokec7 './nba_games.csv'\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf8 \cb3 \strokec8 # Subset Data to 2010 Season, 2014 Season\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 nba_2010\cf4 \strokec4  = \cf5 \strokec5 nba\cf4 \strokec4 [\cf5 \strokec5 nba\cf4 \strokec4 .\cf6 \strokec6 year_id\cf4 \strokec4  == \cf5 \strokec5 2010\cf4 \strokec4 ]\cb1 \
\cf5 \cb3 \strokec5 nba_2014\cf4 \strokec4  = \cf5 \strokec5 nba\cf4 \strokec4 [\cf5 \strokec5 nba\cf4 \strokec4 .\cf6 \strokec6 year_id\cf4 \strokec4  == \cf5 \strokec5 2014\cf4 \strokec4 ]\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 nba_2010\cf4 \strokec4 .\cf6 \strokec6 head\cf4 \strokec4 ())\cb1 \
\cb3 print(\cf5 \strokec5 nba_2014\cf4 \strokec4 .\cf6 \strokec6 head\cf4 \strokec4 ())\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf8 \cb3 \strokec8 #1\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 knicks_pts10\cf4 \strokec4  = \cf5 \strokec5 nba_2010\cf4 \strokec4 .\cf6 \strokec6 pts\cf4 \strokec4 [\cf5 \strokec5 nba_2010\cf4 \strokec4 .\cf6 \strokec6 fran_id\cf4 \strokec4  == \cf7 \strokec7 'Knicks'\cf4 \strokec4 ]\cb1 \
\cf5 \cb3 \strokec5 nets_pts10\cf4 \strokec4  = \cf5 \strokec5 nba_2010\cf4 \strokec4 .\cf6 \strokec6 pts\cf4 \strokec4 [\cf5 \strokec5 nba_2010\cf4 \strokec4 .\cf6 \strokec6 fran_id\cf4 \strokec4  == \cf7 \strokec7 'Nets'\cf4 \strokec4 ]\cb1 \
\
\cf5 \cb3 \strokec5 diff_means_2010\cf4 \strokec4  = \cf5 \strokec5 np\cf4 \strokec4 .\cf6 \strokec6 mean\cf4 \strokec4 (\cf5 \strokec5 knicks_pts10\cf4 \strokec4 ) - \cf5 \strokec5 np\cf4 \strokec4 .\cf6 \strokec6 mean\cf4 \strokec4 (\cf5 \strokec5 nets_pts10\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 diff_means_2010\cf4 \strokec4 )\cb1 \
\
\
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 hist\cf4 \strokec4 (\cf5 \strokec5 knicks_pts10\cf4 \strokec4 , \cf5 \strokec5 alpha\cf4 \strokec4 =\cf5 \strokec5 0.8\cf4 \strokec4 , \cf5 \strokec5 normed\cf4 \strokec4  = \cf2 \strokec2 True\cf4 \strokec4 , \cf5 \strokec5 label\cf4 \strokec4 =\cf7 \strokec7 'knicks'\cf4 \strokec4 )\cb1 \
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 hist\cf4 \strokec4 (\cf5 \strokec5 nets_pts10\cf4 \strokec4 , \cf5 \strokec5 alpha\cf4 \strokec4 =\cf5 \strokec5 0.8\cf4 \strokec4 , \cf5 \strokec5 normed\cf4 \strokec4  = \cf2 \strokec2 True\cf4 \strokec4 , \cf5 \strokec5 label\cf4 \strokec4 =\cf7 \strokec7 'nets'\cf4 \strokec4 )\cb1 \
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 legend\cf4 \strokec4 ()\cb1 \
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 show\cf4 \strokec4 ()\cb1 \
\
\
\
\
\pard\pardeftab720\sl480\partightenfactor0
\cf8 \cb3 \strokec8 #1\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 knicks_pts14\cf4 \strokec4  = \cf5 \strokec5 nba_2014\cf4 \strokec4 .\cf6 \strokec6 pts\cf4 \strokec4 [\cf5 \strokec5 nba_2014\cf4 \strokec4 .\cf6 \strokec6 fran_id\cf4 \strokec4  == \cf7 \strokec7 'Knicks'\cf4 \strokec4 ]\cb1 \
\cf5 \cb3 \strokec5 nets_pts14\cf4 \strokec4  = \cf5 \strokec5 nba_2014\cf4 \strokec4 .\cf6 \strokec6 pts\cf4 \strokec4 [\cf5 \strokec5 nba_2014\cf4 \strokec4 .\cf6 \strokec6 fran_id\cf4 \strokec4  == \cf7 \strokec7 'Nets'\cf4 \strokec4 ]\cb1 \
\
\cf5 \cb3 \strokec5 diff_means_2014\cf4 \strokec4  = \cf5 \strokec5 np\cf4 \strokec4 .\cf6 \strokec6 mean\cf4 \strokec4 (\cf5 \strokec5 knicks_pts14\cf4 \strokec4 ) - \cf5 \strokec5 np\cf4 \strokec4 .\cf6 \strokec6 mean\cf4 \strokec4 (\cf5 \strokec5 nets_pts14\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 diff_means_2014\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 clf\cf4 \strokec4 ()\cb1 \
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 hist\cf4 \strokec4 (\cf5 \strokec5 knicks_pts14\cf4 \strokec4 , \cf5 \strokec5 alpha\cf4 \strokec4 =\cf5 \strokec5 0.8\cf4 \strokec4 , \cf5 \strokec5 normed\cf4 \strokec4  = \cf2 \strokec2 True\cf4 \strokec4 , \cf5 \strokec5 label\cf4 \strokec4 =\cf7 \strokec7 'knicks'\cf4 \strokec4 )\cb1 \
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 hist\cf4 \strokec4 (\cf5 \strokec5 nets_pts14\cf4 \strokec4 , \cf5 \strokec5 alpha\cf4 \strokec4 =\cf5 \strokec5 0.8\cf4 \strokec4 , \cf5 \strokec5 normed\cf4 \strokec4  = \cf2 \strokec2 True\cf4 \strokec4 , \cf5 \strokec5 label\cf4 \strokec4 =\cf7 \strokec7 'nets'\cf4 \strokec4 )\cb1 \
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 legend\cf4 \strokec4 ()\cb1 \
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 show\cf4 \strokec4 ()\cb1 \
\
\
\pard\pardeftab720\sl480\partightenfactor0
\cf8 \cb3 \strokec8 #Boxplot\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 clf\cf4 \strokec4 () \cf8 \strokec8 #to clear the previous plot\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 sns\cf4 \strokec4 .\cf6 \strokec6 boxplot\cf4 \strokec4 (\cf5 \strokec5 data\cf4 \strokec4  = \cf5 \strokec5 nba_2010\cf4 \strokec4 , \cf5 \strokec5 x\cf4 \strokec4  = \cf7 \strokec7 'pts'\cf4 \strokec4 , \cf5 \strokec5 y\cf4 \strokec4  = \cf7 \strokec7 'fran_id'\cf4 \strokec4 )\cb1 \
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 show\cf4 \strokec4 ()\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf8 \cb3 \strokec8 #Contingency A+L and H+W are really high ther moght be associated\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 location_result_freq\cf4 \strokec4  = \cf5 \strokec5 pd\cf4 \strokec4 .\cf6 \strokec6 crosstab\cf4 \strokec4 (\cf5 \strokec5 nba_2010\cf4 \strokec4 .\cf6 \strokec6 game_result\cf4 \strokec4 , \cf5 \strokec5 nba_2010\cf4 \strokec4 .\cf6 \strokec6 game_location\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 location_result_freq\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 location_result_proportions\cf4 \strokec4  = \cf5 \strokec5 location_result_freq\cf4 \strokec4  / len(\cf5 \strokec5 nba_2010\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 location_result_proportions\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf8 \cb3 \strokec8 #Expected contingency\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 chi2\cf4 \strokec4 , \cf5 \strokec5 pval\cf4 \strokec4 , \cf5 \strokec5 dof\cf4 \strokec4 , \cf5 \strokec5 expected\cf4 \strokec4  = \cf5 \strokec5 chi2_contingency\cf4 \strokec4 (\cf5 \strokec5 location_result_proportions\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 expected\cf4 \strokec4 )\cb1 \
\cb3 print(\cf5 \strokec5 chi2\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf8 \cb3 \strokec8 # Correaltion \cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 point_diff_forecast_corr\cf4 \strokec4  = \cf5 \strokec5 pearsonr\cf4 \strokec4 (\cf5 \strokec5 nba\cf4 \strokec4 .\cf6 \strokec6 forecast\cf4 \strokec4 , \cf5 \strokec5 nba\cf4 \strokec4 .\cf6 \strokec6 point_diff\cf4 \strokec4 )\cb1 \
\pard\pardeftab720\sl480\partightenfactor0
\cf4 \cb3 print(\cf5 \strokec5 point_diff_forecast_corr\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 clf\cf4 \strokec4 () \cf8 \strokec8 #to clear the previous plot\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 scatter\cf4 \strokec4 (\cf7 \strokec7 'forecast'\cf4 \strokec4 , \cf7 \strokec7 'point_diff'\cf4 \strokec4 , \cf5 \strokec5 data\cf4 \strokec4 =\cf5 \strokec5 nba\cf4 \strokec4 )\cb1 \
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 xlabel\cf4 \strokec4 (\cf7 \strokec7 'Forecasted Win Prob.'\cf4 \strokec4 )\cb1 \
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 ylabel\cf4 \strokec4 (\cf7 \strokec7 'Point Differential'\cf4 \strokec4 )\cb1 \
\cf5 \cb3 \strokec5 plt\cf4 \strokec4 .\cf6 \strokec6 show\cf4 \strokec4 ()\cb1 \
}