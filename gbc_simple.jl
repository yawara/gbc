import Iterators.product
import DataStructures.DefaultDict
using Graphs

function gbc(n::Int)
  lines = (Int,Int,Int)[]
  check_table = DefaultDict(false)

  for (p, q, r) in product(0:(n-1), 0:(n-1), 0:(n-1))
    if p != 0 || q != 0 || r != 0
      if !check_table[(p, q, r)]
        flag = true
        for k in 1:(n-1)
          kp, kq, kr = (k*p)%n, (k*q)%n, (k*r)%n
          check_table[(kp, kq, kr)] = true
          if (kp, kq, kr) == (0, 0, 0); flag = false end
        end
        if flag; push!(lines, (p, q, r)) end
      end
    end
  end

  g = graph(lines, Edge{(Int,Int,Int)}[], is_directed = false)

  for (i, l1) in enumerate(lines)
    for (j, l2) in enumerate(lines)
      if i < j
        if (l1[1]*l2[1]+l1[2]*l2[2]+l1[3]*l2[3])%n == 0
          add_edge!(g, l1, l2)
        end
      end
    end
  end

  return g
end
