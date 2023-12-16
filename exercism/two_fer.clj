(ns two-fer)

(defn two-fer
  ([]
   (two-fer "you"))
  ([name]
   (str "One for " name ", one for me.")))





(defn can-free-prisoner?
  "Returns true if prisoner can be freed, false otherwise."
  [knight-awake? archer-awake? prisoner-awake? dog-present?]
  (or (and (not dog-present?) (prisoner-awake?) (not (knight-awake?)) (not (archer-awake?)))
      (and dog-present? (not (archer-awake?)))))
