# 代码实现
参考  
```shell
lake +leanprover-community/mathlib4:lean-toolchain new <your_project_name> math

lake exe cache get
```

### 在以有代码基础上使用mathlib
一开始写的代码不需要使用 mathlib, 后来因为某些原因又要使用了
1. 修改 leanfile.toml
```shell
[[require]]
name = "mathlib"
scope = "leanprover-community"
``` 
意思是告诉 lake 需要这个依赖

2. 更新
```shell
curl https://raw.githubusercontent.com/leanprover-community/mathlib4/master/lean-toolchain -o lean-toolchain
```