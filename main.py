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
        print("投稿完了")
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

#自身のツイートのみ表示
def display_owned_tweet_only():
    print("----------------------------------------------------------------------")
    for get_tweet in api.user_timeline(api.me().id):
        print("Tweeted by:{}\tTweetID:{}".format(get_tweet.user.screen_name,get_tweet.id))
        print("{}".format(get_tweet.text))
        print("いいね:{}\tRT:{}".format(get_tweet.favorite_count,get_tweet.retweet_count))
        print("投稿日時{}\tクライアント名:{}".format(get_tweet.created_at,get_tweet.source))
        print("----------------------------------------------------------------------")

#選択した自身のツイートを削除
def deleate_owned_tweet():
    select_id=input("削除する自身のツイートのidを入力してください")
    try:
        api.destroy_status(select_id)
        print("削除完了")
    except:
        print("無効なid")

#選択したツイートをいいねする
def like_tweet():
    select_id=input("いいねするツイートのidを入力してください")
    try:
        api.create_favorite(select_id)
        print("いいね完了")
    except:
        print("無効なid")

#選択したツイートをRT
def RT_tweet():
    select_id=input("RTするツイートのidを入力してください")
    try:
        api.retweet(select_id)
        print("RT完了")
    except:
        print("無効なid")

#main
if __name__=='__main__':
    while(True):
        print("選択メニュー")
        select_num=input("1:ツイートの投稿\t2:TLから最新20件の投稿を表示・いいね・RT\n3:自身のツイートのみ20件表示・削除\t4:終了\n")
        if select_num=='1' or select_num=='１':
            print("ツイートの投稿")
            tweet()
        elif select_num=='2' or select_num=='２':
            print("TLから最新20件の投稿を表示・いいね・RT")
            display_home_20tweet()
            print("いいね・RTをする？")
            select_num=input("1:いいね\t2:RT\t3:メニューに戻る\n")
            if select_num=='1' or select_num=='１':
                print("いいね")
                like_tweet()
            elif select_num=='2' or select_num=='２':
                print("RT")
                RT_tweet()
            elif select_num=='3' or select_num=='３':
                print("メニューに戻る")
            else:
                print("無効な入力\n最初からやり直してください")
        elif select_num=='3' or select_num=='３':
            print("自身のツイートのみ20件表示・削除")
            display_owned_tweet_only()
            print("削除をする？")
            select_num=input("1:削除\t2:メニューに戻る\n")
            if select_num=='1' or select_num=='１':
                print("削除")
                deleate_owned_tweet()
            elif select_num=='2' or select_num=='２':
                print("メニューに戻る")
            else:
                print("無効な入力\n最初からやり直してください")
        elif select_num=='4' or select_num=='４':
            print("終了")
            exit()
        else:
            print("無効な入力\n最初からやり直してください")