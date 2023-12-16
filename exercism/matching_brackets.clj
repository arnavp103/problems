(ns matching-brackets)

;; return false if incorrect match
; otherwise return input after closing matched brackets
(defn inner-matcher [input current_opening]
  (let [brackets {\( \) \[ \] \{ \}}]
    (cond
      ;; if input empty and we have a current opening, then we have an unclosed bracket
      (empty? input) false
      (contains? (set (keys brackets)) (first input)) (recur (rest input) (first input))
      (contains? (set (vals brackets)) (first input)) (if (= (get brackets current_opening) (first input))
                                                        (rest input)
                                                        false)
      :else (recur (rest input) current_opening))))


(defn valid? [input]
  (let [opening-brackets #{\( \[ \{}]
    (loop [input input]
      (cond
        (empty? input) true
        (contains? opening-brackets (first input)) (let [inner-match (inner-matcher (rest input) (first input))]
                                                     (if (not inner-match)
                                                       false
                                                       (recur inner-match)))
        :else (recur (rest input))))))

