# should put your own shell interpreter path here 

echo -e "\e[1;32mtweetvid_download is running ...\e[0m"

if command -v python >/dev/null ; then
    echo -e "\e[1;32mdependency: python satisfied\e[0m"
else   
    echo -e "\e[1;31mNeed to download python first, go check\e[0m \e[1;36mhttps://www.python.org/downloads/ \e[0m"
    exit
fi

if command -v pip3>/dev/null; then
    echo -e "\e[1;32mdependency: pip/pip3 satisfied\e[0m"
else
    echo -e "\e[1;31mNeed to download pip/pip3 first, go check\e[0m \e[1;36mhttps://www.python.org/downloads/ \e[0m"
    exit
fi

if pip show --files requests>/dev/null; then
    echo -e "\e[1;32mdependency: python lib requests satisfied\e[0m"
else
    echo -e "\e[1;31mNeed to install requests first, run script\e[0m \e[1;36mpip3 install requests\e[0m"
    pip3 install requests
fi

if pip show --files selenium>/dev/null; then
    echo -e "\e[1;32mdependency: python lib selenium satisfied\e[0m"
else
    echo -e "\e[1;31mNeed to install selenium first, run script\e[0m \e[1;36mpip3 install selenium\e[0m"
    pip3 install requests
fi

if pip show --files GetOldTweets3>/dev/null; then
    echo -e "\e[1;32mdependency: python lib GetOldTweets3 satisfied\e[0m"
else
    echo -e "\e[1;31mNeed to install GetOldTweets3 first, run script\e[0m \e[1;36mpip3 install GetOldTweets3\e[0m"
    pip3 install GetOldTweets3
fi

echo -e "\e[1;32mall dependecies satisfied\e[0m"

echo -e "\e[1;32m1. get the tweet list of a user\e[0m"

echo -e -n "\e[1;33mEnter the user name here: \e[0m"
read user_name
echo -e -n "\e[1;33mEnter the maximum number of tweets you want to check (int, better <= 1000): \e[0m"
read max_num
echo -e "\e[1;33mBegin collecting the tweet links ...\e[0m"
python get_twlist.py -u $user_name -n $max_num
echo -e "\e[1;32m2. get a list of tweets containing video files\e[0m"
echo -e "\e[1;33mBegin collecting the video links ...\e[0m"
echo -e -n "\e[1;33mShow the checking process (y/n):\e[0m"
read arg

if [ $arg = "y" -o $arg = "Y" ]; then
    python get_vidlist.py -u $user_name
else
    python get_vidlist.py -u $user_name >/dev/null
fi

file_name=$user_name"_vid_list.txt"
line=`sed -n '$=' $file_name`
echo -e $line video links have been collected, the results can be found in $file_name
echo -e "\e[1;32m3. download video files\e[0m"
echo -e "\e[1;33mBegin downloading the .mp4 files ...\e[0m"
python dl_vid.py -u $user_name
folder_name=$user_name"_vid_data"
echo -e "\e[1;32mDownload complete, the videos are saved in folder $folder_name\e[0m"
#echo wmic cpu get NumberOfLogicalProcessors

