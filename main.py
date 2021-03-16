import APIKey,AccessToken
import tweepy

#トークンの読み込み
#アカウント切り替え実装時に入れ替えられる
api_key=APIKey.api
api_key_secrert=APIKey.secret
access_token=AccessToken.token
access_token_secret=AccessToken.secret

#認証
auth=tweepy.OAuthHandler(api_key,api_key_secrert)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

#ツイート
def tweet():
    text=input("いまどうしてる?\n")
    if len(text)>140:
        print("全角・半角問わず140文字以内に収めてください\n")
        tweet()
    elif len(text)==0:
        print("未入力です.最初からやり直してください")
    else:
        print("完了")
        api.update_status(text)

#タイムラインの表示(20件)
def display_home_20tweet():
    print("----------------------------------------------------------------------")
    for get_tweet in api.home_timeline():
        print("Tweeted by:{}\tTweetID:{}".format(get_tweet.user.screen_name,get_tweet.id))
        print("{}".format(get_tweet.text))
        print("いいね:{}\tRT:{}".format(get_tweet.favorite_count,get_tweet.retweet_count))
        print("投稿日時{}\tクライアント名:{}".format(get_tweet.created_at,get_tweet.source))
        print("----------------------------------------------------------------------")

#main
if __name__=='__main__':
    while(True):
        print("選択メニュー")
        select_num=input("1:ツイート\t2:TLから最新20件の投稿を表示\t3:終了\n")
        if select_num=='1' or select_num=='１':
            print("ツイート")
            tweet()
        elif select_num=='2' or select_num=='２':
            print("TLから最新20件の投稿を表示")
            display_home_20tweet()
        elif select_num=='3' or select_num=='３':
            print("終了")
            exit()
        else:
            print("無効な入力\n最初からやり直してください")