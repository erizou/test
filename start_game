@app.route('/start_game', methods=['GET'])
def start_game():
    characters = ["鈴木 壱郎", "鈴木 次郎", "鈴木 三郎太", "鈴木 四乃", "鈴木 いつき"]
    stats = generate_balanced_stats(["talk", "sing", "dance", "acting", "teamwork"])
    player = {
        "名前": "主人公",
        "年齢": random.randint(14, 18),
        "stats": stats,
        "favorability": {name: 0 for name in characters}
    }
    return jsonify(player)
