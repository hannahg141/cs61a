; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

;predicate, if true, if false
;everything except #f is True
;we can use True and False *
;if else (taken to be True) if no pred is True do this

(define (sign x)
  (cond
    ((< x 0) -1)
    ((> x 0) 1)
    (else 0))
)

(define (ordered? s)
    (cond
        ((null? s) True)
        ((null? (cdr s)) True)
        ((<= (car s) (cadr s)) (ordered? (cdr s)))
        (else False)
    )
)


(define (nodots s)
    (if (null? s) 
        nil 
        (if (number? s) 
            (cons s nil) 
            (if (pair? (car s)) 
                (cons (nodots (car s)) (nodots (cdr s ))) ;call nodots each time to make sure not a NESTED pair?*
                (if (number? (cdr s)) 
                    (cons (car s ) (cons (cdr s) nil)) 
                    (cons (car s ) (nodots (cdr s))) 
                )
            )
        )
    )
)


; Sets as sorted lists
; a set is a scheme list with no repeated elements, ordered from least to greatest

(define (empty? s) (null? s))

;takes in a set and value v
;adds the v to s. NO REPEATS

(define (contains? s v)
    (cond ((empty? s) false)
        ((= (car s) v) true)
        ((> (car s) v) false)
        (else (contains? (cdr s) v)) ; replace this line
    )
)

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (cond ((empty? s) (list v))
        ((contains? s v) s)
        ((> (car s) v) (cons v s))
        (else (cons (car s) (add (cdr s) v))) 
    )
)

(define (intersect s t)
    (cond ((or (empty? s) (empty? t)) nil)
          ((= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t))))
            ((> (car s) (car t)) (intersect s (cdr t)))
          ((< (car s) (car t)) (intersect (cdr s) t))
    )
)


; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          ((= (car s) (car t)) (cons (car s) (union (cdr s) (cdr t))))
          ((> (car s) (car t)) (cons (car t) (union s (cdr t))))
            ((< (car s) (car t)) (cons (car s) (union (cdr s) t)))
    )
)

; Tail-Calls in Scheme

(define (exp-recursive b n)
  (if (= n 0)
      1
      (* b (exp-recursive b (- n 1)))))

(define (exp b n)
  ;; Computes b^n.
  ;; b is any number, n must be a non-negative integer.
    (define (exponent-helper b n total)
        (if (= n 0)
            total
            (exponent-helper b (- n 1) (* b total)))
    )
    (exponent-helper b n 1)
)



(define (filter pred lst)
    (define (filter-helper pred lst new)
        (cond ((null? lst) 
                        new)
            ((pred (car lst)) (filter-helper pred (cdr lst) (append new (list(car lst)))))
            (else (filter-helper pred (cdr lst) new))
        )
    )
    (filter-helper pred lst nil)
)


