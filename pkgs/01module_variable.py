#module_variable.py
a = 3
b = 2
c = "hello"
print(a*2+b)
print(c*2)

print("A", end="")
print("B") #default end="\n"
print("B")
print("C")
print(a, "EFG" + "H")

age = 20
name="아무개"
print(name, "는", age, "살 입니다.") #숫자와 글자는 + 연산자로 안 붙여진다.
print("%s는 %d살 입니다." %(name, age))
print("integer: %d string: %s" %(10,"하잉"))

#age = input("나이는?")
print(int(age) + 3) #input값은 무조건 string으로 변환하여 받음.
#타입(형)변환 : Casting

# list, tuple, dictionary
# list = 배열 : 여러 값을 담기 위한 변수
list = [1, 2, 3, 4, [5, 6, 7]]
print(len(list))
print(list[len(list)-1]) #전체 length에 -1하면 마지막 index 번호가 됨.
print(list[4][1]) # n차원 index
print(list[-1])
list.append('a')
print(list[3]) #1, 2, 3, 5
list[2] = 4
list.remove('a')
del list[0]
print(list)

# tuple : list의 상수(고정불변)
tupl = (1, 2, 3)

# dictionary
# JSON 표기법 : {key : value}, javascript object notation
dic = {"uid":"kim", "upw":"111", "gen":"f"}
print(dic["uid"])
dic["addr"] = "seoul"
dic["addr"] = "incheon"
print(dic)
#remove 함수 지원 X
del dic["addr"]
print(dic)
tt = dic.keys()
print(type(tt))

for k in tt:
    print(k)


video = {
 "kind": "youtube#videoListResponse",
 "etag": "\"UCBpFjp2h75_b92t44sqraUcyu0/sDAlsG9NGKfr6v5AlPZKSEZdtqA\"",
 "videos": [
  {
   "id": "7lCDEYXw3mM",
   "kind": "youtube#video",
   "etag": "\"UCBpFjp2h75_b92t44sqraUcyu0/iYynQR8AtacsFUwWmrVaw4Smb_Q\"",
   "snippet": {
    "publishedAt": "2012-06-20T22:45:24.000Z",
    "channelId": "UC_x5XG1OV2P6uZZ5FSM9Ttw",
    "title": "Google I/O 101: Q&A On Using Google APIs",
    "description": "Antonio Fuentes speaks to us and takes questions on working with Google APIs and OAuth 2.0.",
    "thumbnails": {
                     "default": {
                      "url": "https://i.ytimg.com/vi/7lCDEYXw3mM/default.jpg"
                     },
                     "medium": {
                      "url": "https://i.ytimg.com/vi/7lCDEYXw3mM/mqdefault.jpg"
                     },
                     "high": {
                      "url": "https://i.ytimg.com/vi/7lCDEYXw3mM/hqdefault.jpg"
                     }
                    },
                "categoryId": "28"
               },
               "contentDetails": {
                "duration": "PT15M51S",
                "aspectRatio": "RATIO_16_9"
               },
               "statistics": {
                "viewCount": "3057",
                "likeCount": "25",
                "dislikeCount": "0",
                "favoriteCount": "17",
                "commentCount": "12"
               },
               "status": {
                "uploadStatus": "STATUS_PROCESSED",
                "privacyStatus": "PRIVACY_PUBLIC"
               }
  }
 ]
}

print(video["videos"][0]["id"])
print(video["videos"][0]["snippet"]["title"])
print(video["videos"][0]["snippet"]["thumbnails"]["default"]["url"])





