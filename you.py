import random
characters = ["鈴木 壱郎", "鈴木 次郎", "鈴木 三郎太", "鈴木 四乃", "鈴木 いつき"]

主人公 = {
    "名前": "主人公",
    "年齢": random.randint(14, 18),
    "stats": {
        "talk": random.randint(1, 3), 
        "sing": random.randint(1, 3), 
        "dance": random.randint(1, 3), 
        "acting": random.randint(1, 3), 
        "teamwork": random.randint(1, 3) 
    },
    "favorability": {name: 0 for name in characters}
}
