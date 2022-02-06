{\rtf1\ansi\ansicpg1252\cocoartf2580
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red129\green131\blue134;\red23\green23\blue23;\red255\green255\blue255;
\red164\green191\blue255;\red252\green115\blue96;\red117\green255\blue242;\red254\green219\blue112;}
{\*\expandedcolortbl;;\cssrgb\c57647\c58431\c59608;\cssrgb\c11765\c11765\c11765;\cssrgb\c100000\c100000\c100000;
\cssrgb\c70196\c80000\c100000;\cssrgb\c100000\c53725\c45098;\cssrgb\c51373\c100000\c96078;\cssrgb\c100000\c87843\c51373;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl480\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 # import codecademylib3\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf5 \cb3 \strokec5 import\cf4 \strokec4  \cf6 \strokec6 codecademylib3\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 import\cf4 \strokec4  \cf6 \strokec6 numpy\cf4 \strokec4  \cf5 \strokec5 as\cf4 \strokec4  \cf6 \strokec6 np\cf4 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 from\cf4 \strokec4  \cf6 \strokec6 matplotlib\cf4 \strokec4  \cf5 \strokec5 import\cf4 \strokec4  \cf6 \strokec6 pyplot\cf4 \strokec4  \cf5 \strokec5 as\cf4 \strokec4  \cf6 \strokec6 plt\cf4 \cb1 \strokec4 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb3 \strokec2 # load in data\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf6 \cb3 \strokec6 in_bloom\cf4 \strokec4  = \cf6 \strokec6 np\cf4 \strokec4 .\cf7 \strokec7 loadtxt\cf4 \strokec4 (open(\cf8 \strokec8 "in-bloom.csv"\cf4 \strokec4 ), \cf6 \strokec6 delimiter\cf4 \strokec4 =\cf8 \strokec8 ","\cf4 \strokec4 )\cb1 \
\cf6 \cb3 \strokec6 flights\cf4 \strokec4  = \cf6 \strokec6 np\cf4 \strokec4 .\cf7 \strokec7 loadtxt\cf4 \strokec4 (open(\cf8 \strokec8 "flights.csv"\cf4 \strokec4 ), \cf6 \strokec6 delimiter\cf4 \strokec4 =\cf8 \strokec8 ","\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb3 \strokec2 # Plot many histograms\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf6 \cb3 \strokec6 plt\cf4 \strokec4 .\cf7 \strokec7 figure\cf4 \strokec4 (\cf6 \strokec6 1\cf4 \strokec4 )\cb1 \
\cf6 \cb3 \strokec6 plt\cf4 \strokec4 .\cf7 \strokec7 subplot\cf4 \strokec4 (\cf6 \strokec6 211\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb3 \strokec2 #Flights plot\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf6 \cb3 \strokec6 plt\cf4 \strokec4 .\cf7 \strokec7 hist\cf4 \strokec4 (\cf6 \strokec6 flights\cf4 \strokec4 , range=(\cf6 \strokec6 0\cf4 \strokec4 ,\cf6 \strokec6 365\cf4 \strokec4 ),\cf6 \strokec6 bins\cf4 \strokec4 =\cf6 \strokec6 365\cf4 \strokec4 )\cb1 \
\cf6 \cb3 \strokec6 plt\cf4 \strokec4 .\cf7 \strokec7 title\cf4 \strokec4 (\cf8 \strokec8 "Histogram of flights"\cf4 \strokec4 )\cb1 \
\cf6 \cb3 \strokec6 plt\cf4 \strokec4 .\cf7 \strokec7 xlabel\cf4 \strokec4 (\cf8 \strokec8 "Days of year"\cf4 \strokec4 )\cb1 \
\cf6 \cb3 \strokec6 plt\cf4 \strokec4 .\cf7 \strokec7 ylabel\cf4 \strokec4 (\cf8 \strokec8 "Counts"\cf4 \strokec4 )\cb1 \
\
\
\
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb3 \strokec2 #Flowers bloom plot\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf6 \cb3 \strokec6 plt\cf4 \strokec4 .\cf7 \strokec7 subplot\cf4 \strokec4 (\cf6 \strokec6 212\cf4 \strokec4 )\cb1 \
\cf6 \cb3 \strokec6 plt\cf4 \strokec4 .\cf7 \strokec7 hist\cf4 \strokec4 (\cf6 \strokec6 in_bloom\cf4 \strokec4 , range=(\cf6 \strokec6 0\cf4 \strokec4 ,\cf6 \strokec6 365\cf4 \strokec4 ), \cf6 \strokec6 bins\cf4 \strokec4 =\cf6 \strokec6 365\cf4 \strokec4 )\cb1 \
\cf6 \cb3 \strokec6 plt\cf4 \strokec4 .\cf7 \strokec7 title\cf4 \strokec4 (\cf8 \strokec8 "Histogram of flowers"\cf4 \strokec4 )\cb1 \
\cf6 \cb3 \strokec6 plt\cf4 \strokec4 .\cf7 \strokec7 xlabel\cf4 \strokec4 (\cf8 \strokec8 "Days of year"\cf4 \strokec4 )\cb1 \
\cf6 \cb3 \strokec6 plt\cf4 \strokec4 .\cf7 \strokec7 ylabel\cf4 \strokec4 (\cf8 \strokec8 "Counts"\cf4 \strokec4 )\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb3 \strokec2 #To prevent labels to overlap with the graphs\cf4 \cb1 \strokec4 \
\pard\pardeftab720\sl480\partightenfactor0
\cf6 \cb3 \strokec6 plt\cf4 \strokec4 .\cf7 \strokec7 tight_layout\cf4 \strokec4 ()\cb1 \
\cf6 \cb3 \strokec6 plt\cf4 \strokec4 .\cf7 \strokec7 show\cf4 \strokec4 ()\cb1 \
\
\pard\pardeftab720\sl480\partightenfactor0
\cf2 \cb3 \strokec2 #The best time to visit Acadia, Maine when is not crowded and while flowers while floors were blooming is during September-October-November-December (Fall).\cf4 \cb1 \strokec4 \
\
}