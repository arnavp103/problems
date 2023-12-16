(ns robot-simulator)

(defn robot
  [coordinates dir]
  {:bearing dir,
   :coordinates coordinates})


(defn right-rotate [{:keys [bearing]
                     {:keys [x y]} :coordinates}]
  (cond (= bearing :north) (robot {:x x :y y} :east)
        (= bearing :east)  (robot {:x x :y y} :south)
        (= bearing :south) (robot {:x x :y y} :west)
        :else              (robot {:x x :y y} :north)))

(defn left-rotate [{:keys [bearing]
                    {:keys [x y]} :coordinates}]
  (cond (= bearing :north) (robot {:x x :y y} :west)
        (= bearing :west)  (robot {:x x :y y} :south)
        (= bearing :south) (robot {:x x :y y} :east)
        :else              (robot {:x x :y y} :north)))

(defn advance [{:keys [bearing]
                {:keys [x y]} :coordinates}]
  (cond (= bearing :east)   (robot {:x (+ x 1) :y y} bearing)
        (= bearing :north)  (robot {:x x :y (+ y 1)} bearing)
        (= bearing :west)   (robot {:x (- x 1) :y y} bearing)
        :else               (robot {:x x :y (- y 1)} bearing)))


(defn simulate
  [moves robot]
  (reduce
   (fn [rbt move]
     (cond (= move \R) (right-rotate rbt)
           (= move \L) (left-rotate rbt)
           (= move \A) (advance rbt)))
   robot moves))


