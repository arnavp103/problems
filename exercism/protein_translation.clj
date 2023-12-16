(ns protein-translation)

;; AUG 	Methionine
;; UUU, UUC 	Phenylalanine
;; UUA, UUG 	Leucine
;; UCU, UCC, UCA, UCG 	Serine
;; UAU, UAC 	Tyrosine
;; UGU, UGC 	Cysteine
;; UGG 	Tryptophan
;; UAA, UAG, UGA 	STOP

;; theres more but unneeded for the exercise
(defn translate-codon [codon]
  (case codon
    "AUG" "Methionine"
    "UUU" "Phenylalanine"
    "UUC" "Phenylalanine"
    "UUA" "Leucine"
    "UUG" "Leucine"
    "UCU" "Serine"
    "UCC" "Serine"
    "UCA" "Serine"
    "UCG" "Serine"
    "UAU" "Tyrosine"
    "UAC" "Tyrosine"
    "UGU" "Cysteine"
    "UGC" "Cysteine"
    "UGG" "Tryptophan"
    "UAA" "STOP"
    "UAG" "STOP"
    "UGA" "STOP"))

(defn translate-rna [rna]
  (let [codons (map (partial apply str) (partition 3 rna))]
    (reduce (fn [acc codon]
              (let [protein (translate-codon codon)]
                (if (= protein "STOP")
                  (reduced acc)
                  (conj acc protein))))
            []
            codons)))

