import Iterators.product
import DataStructures.DefaultDict
using Graphs

include("Zmods.jl")
using Zmods

function gbc{T<:Integer}(n::T)
  lines = Vector{zmod{n, typeof(n)}}[]
  check_table = DefaultDict(false)

  for (p, q, r) in product(Zmod(n), Zmod(n), Zmod(n))
    if !check_table[(p, q, r)]
      flag = true
      for k in Zmod(n)
        if k != 0
          kp, kq, kr = k*p, k*q, k*r
          check_table[(kp, kq, kr)] = true
          if (kp, kq, kr) == (0, 0, 0); flag = false end
        end
      end
      if flag; push!(lines, [p, q, r]) end
    end
  end

  g = graph(lines, Edge{Vector{zmod{n, typeof(n)}}}[], is_directed = false)

  for (i, l1) in enumerate(lines)
    for (j, l2) in enumerate(lines)
      if i < j
        if dot(l1, l2) == 0
          add_edge!(g, l1, l2)
        end
      end
    end
  end

  return g
end
