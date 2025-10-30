# Checks if an integer is even
is.even <- function(n = 2) {
  if (n %% 2 == 0) {
    return(paste(n,'is even!'))
  } else {
    return(paste(n,'is odd!'))
  }
}

is.even(6)

#Test
print(is.even(6))   # 6 is even!
print(is.even(7))   # 7 is odd!

# Checks if a number is a power of 2
is.power2 <- function(n = 2) {
  if (log2(n) %% 1==0) {
    return(paste(n, 'is a power of 2!'))
  } else {
    return(paste(n,'is not a power of 2!'))
  }
}

is.power2(4)

#Test
print(is.power2(4))   # 4 is a power of 2!
print(is.power2(6))   # 6 is not a power of 2!

# Checks if a number is prime
is.prime <- function(n) {
  if (n==0) {
    return(paste(n,'is a zero!'))
  } else if (n==1) {
    return(paste(n,'is just a unit!'))
  }
  
  ints <- 2:(n-1)
  
  if (all(n%%ints!=0)) {
    return(paste(n,'is a prime!'))
  } else {
    return(paste(n,'is a composite!'))
  }
}

is.prime(3)

#Test
print(is.prime(3))   # 3 is a prime!
print(is.prime(9))   # 9 is a composite!
print(is.prime(1))   # 1 is just a unit!