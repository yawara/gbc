module Zmods
  import Iterators.imap

  export zmod, Zmod

  immutable zmod{N,T<:Integer}
    num::T
  end

  +{N,T<:Integer}(a::zmod{N,T}, b::zmod{N,T}) = zmod{N,T}((a.num + b.num)%N)
  +{N,T<:Integer}(a::T, b::zmod{N,T}) = zmod{N,T}((a + b.num)%N)
  +{N,T<:Integer}(a::zmod{N,T}, b::T) = zmod{N,T}((a.num + b)%N)
  *{N,T<:Integer}(a::zmod{N,T}, b::zmod{N,T}) = zmod{N,T}((a.num * b.num)%N)
  *{N,T<:Integer}(a::T, b::zmod{N,T}) = zmod{N,T}((a * b.num)%N)
  *{N,T<:Integer}(a::zmod{N,T}, b::T) = zmod{N,T}((a.num * b)%N)
  *{N, T<:Integer}(a::zmod{N,T}, v::Vector{zmod{N,T}}) = [ a*v[1], a*v[2], a*v[3] ]
  =={N,T<:Integer}(a::zmod{N,T}, b::zmod{N,T}) = (a.num - b.num)%N==0
  =={N,T<:Integer}(a::T, b::zmod{N,T}) = (a - b.num)%N==0
  =={N,T<:Integer}(a::zmod{N,T}, b::T) = (a.num - b)%N==0
  !={N,T<:Integer}(a::zmod{N,T}, b::zmod{N,T}) = (a.num - b.num)%N!=0
  !={N,T<:Integer}(a::T, b::zmod{N,T}) = (a - b.num)%N!=0
  !={N,T<:Integer}(a::zmod{N,T}, b::T) = (a.num - b)%N!=0

  Zmod{T<:Integer}(n::T, is_plus = false) = imap( x -> zmod{n, T}(x), 0:(n-1) )

end
