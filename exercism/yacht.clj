
(ns yacht)

(defn full-house? [dice]
  (let [counts (frequencies dice)]
    (and (= 2 (count counts))
         (some #(= 3 (counts %)) (keys counts)))))

(defn four-of-a-kind [dice]
  (let [counts (frequencies dice)
        max-count (apply max (vals counts))
        max-key (if (= 4 (counts (first (keys counts))))
                  (first (keys counts))
                  (last (keys counts)))]
    (if (>= max-count 4)
      (* 4 max-key)
      0)))


(defn little-straight? [dice]
  (= (sort dice) [1 2 3 4 5]))

(defn big-straight? [dice]
  (= (sort dice) [2 3 4 5 6]))

(defn yacht? [dice]
  (apply = dice))

(defn score [dice cat]
  (case cat
    "ones" (apply + (filter #(= % 1) dice))
    "twos" (apply + (filter #(= % 2) dice))
    "threes" (apply + (filter #(= % 3) dice))
    "fours" (apply + (filter #(= % 4) dice))
    "fives" (apply + (filter #(= % 5) dice))
    "sixes" (apply + (filter #(= % 6) dice))
    "full house" (if (full-house? dice) (apply + dice) 0)
    "four of a kind" (four-of-a-kind dice)
    "little straight" (if (little-straight? dice) 30 0)
    "big straight" (if (big-straight? dice) 30 0)
    "choice" (apply + dice)
    "yacht" (if (yacht? dice) 50 0)
    0))
