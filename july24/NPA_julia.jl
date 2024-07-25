using Pkg; Pkg.add(url="https://github.com/ewoodhead/QuantumNPA.jl"); 
using QuantumNPA


A1, A2, A3, A4 = dichotomic(1, 1:4)
B1, B2, B3 = dichotomic(2, 1:2)
C1 = dichotomic(3, 1)
ops1 = [Id, A1, A2, B1, B2, C1]
ops2 = sort(Set(O1*O2 for O1 in ops1 for O2 in ops1))

indices = Dict()

indexed_ops = collect(enumerate(ops2))

for (i, x) in indexed_ops
    for (j, y) in indexed_ops[i:end]
        m = conj(x)*y
        m = min(m, conj(m))

        if haskey(indices, m)
            push!(indices[m], (i, j))
        else
            indices[m] = [(i, j)]
        end
    end
end

for (m, l) in sort!(collect(indices), by=first)
    @printf "%11s  =>  %s\n" m l
end