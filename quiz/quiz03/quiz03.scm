; Load this file into an interactive session with:
; python3 scheme -load quiz03.scm

; Filter (from lab) takes a predicate procedure f and a list s. It returns a
; new list containing only elements x in s for which (f x) is a true value.
(define (filter f s)
    (cond ((null? s) '())
          ((f (car s)) (cons (car s) (filter f (cdr s))))
          (else (filter f (cdr s))))
)

; All takes a predicate procedure f and a list s. It returns whether (f x) is
; a true value for every element x in s.
(define (all f s)
    (cond ((null? s) True)
          (else (and (f (car s)) (all f (cdr s))))
      )
)

; Every takes a two-argument predicate g and a list s. It returns a new list
; containing only elements x in s for which (g x y) is true for every y in s.
(define (every g s)
    (define (every-iter x)
        (all (lambda (y) (g x y)) s)
      )
      (filter every-iter s)
)

; Return a minimum card.
(define (min hand) (car (every <= hand)))

; Fimp returns the card played under the fimping strategy in Cucumber.
(define (fimp hand highest)
    (if (null? (every <= (filter (lambda (y) (>= y highest)) hand)))
        (min hand)
        (if (<= highest (car (every <= (filter (lambda (y) (>= y highest)) hand))))
            (car (every <= (filter (lambda (y) (>= y highest)) hand)))
            (car (every >= hand))
          )
    )
)


; Legal returns pairs of (card . control) for all legal plays in Cucumber.
(define (legal hand highest)
  (define least (min hand))
  (define (result hand)
    (if (null? hand) nil (begin
        (define card (car hand))
        (define (pairs c) (cons c (>= c highest)))
        (if (or (>= card highest) (eq? card least))
            (cons (pairs card) (result (cdr hand)))
            (result (cdr hand))
            )
        )))
  (result hand))
