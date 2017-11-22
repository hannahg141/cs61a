;; Scheme ;;
(define (accumulate combiner start n term)
  (if (= n 0)
      start
      (combiner (accumulate combiner start (- n 1) term)
      			(term n)
      )
   )
)



;;; Tests
(define (identity x) x)
(accumulate * 1 5 identity)
; expect 120

(define (square x) (* x x))
(accumulate + 0 5 square)
; expect 55

(define (how-many-dots s)
  (cond ((null? s) 0)
  		((number? (car s)) how-many-dots (cdr s))
  		((pair? (car s)) 1)
  )
)

;;; Tests

(how-many-dots '(1 2 3))
; expect 0
(how-many-dots '(1 2 . 3))
; expect 1
(how-many-dots '((1 . 2) 3 . 4))
; expect 2
(how-many-dots '((((((1 . 2) . 3) . 4) . 5) . 6) . 7))
; expect 6
(how-many-dots '(1 . (2 . (3 . (4 . (5 . (6 . (7))))))))
; expect 0



(define (swap s)
	(define (help-swap so-far remaining)
		(cond ((null? s) so-far)
				((null (cdr s)) )
			(help-swap (cdr (cdr s)) (list (car (cdr s)) (car s)
									)
			)
		)
	)
  (help-swap s nil)
)

;;; Tests

(swap (list 1 2 3 4))
; expect (2 1 4 3)
(swap (list 1 2 3 4 5))
; expect (2 1 4 3 5)