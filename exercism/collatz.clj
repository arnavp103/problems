(ns collatz-conjecture)

(defn helper [n c]
  (cond (= n 1) c
        (even? n) (helper (/ n 2) (+ c 1))
        :else (helper (+ (* n 3) 1) (+ c 1))))

(defn collatz [num]
  (helper num 0))
