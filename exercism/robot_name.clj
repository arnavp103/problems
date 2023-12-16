(ns robot-name)


(defn robot []
  (let [letters (map char (range 65 91))
        numbers (map str (range 1000))
        name (str (rand-nth letters) (rand-nth letters) (rand-nth numbers))]
    {:name name}))

(defn robot-name [robot]
  (:name robot))

(defn reset-name [old]
  (let [letters (map char (range 65 91))
        numbers (map str (range 1000))
        name (str (rand-nth letters) (rand-nth letters) (rand-nth numbers))]
    (if (= (robot-name old) name)
      (reset-name old)
      ;; mutate the robot
      (swap! old assoc :name name))))


