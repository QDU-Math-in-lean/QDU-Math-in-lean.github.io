## 问题描述

我有一个A24.0文件 里面用的是24.0版本的lean以及对应的mathlib
那么A24.0文件中就有一个6g大的.lake
如果我要创建一个B24.0文件,我需要使用

```bash
lake new B24.0 math.lean
```

关于 [[lake 常用指令]]

它会创建一个 B24.0 文件里面有一个完整的 mathlib库,又是6g
这非常占用空间

lean有没有办法做成和其他包管理器一样,把依赖包都统一放到一个位置而不是分散在每一个小文件中呢?

## 使用符号链接

lakefile.lean 中 依赖是:

```lean
require "leanprover-community" / "mathlib" @ "git#v4.24.0-rc1"
```

这样写的,那么它要的mathlib就从网站上拉下来



我们可以使用

```bash
lake new B24.0 std.lean # 创建 使用std模板创建 lakefile.lean 的文件

cd Bpath

code . 

# 打开 code 并且 restart file ,这会自动创建一个 .lake

ln -s Apath/.lake/packages/ Bpath/.lake/ # 创建从A24.0 中.lake/packages/ 到 B24.0 .lake的一个 符号连接
```

这相当于 B24.0 的 mathlib文件在 A24.0 中,那么我们仅仅需要一个 6g的mathlib即可

## 更进一步管理

当我们有复数个不同版本的本地库的时候,以上管理方法就不好用了
因为删除一个库,可能会导致下游库符号连接失效

然而

目前 lean 并没有像

```bash
export LAKE_PACKAGES_DIR=$HOME/.lake-packages
```

这样写在 .bashrc 中的指令
也就是没有一个管理所有依赖的 .lake-packages ,以便于我们所有的 mathlib从.lake-packages 中获取

所以 

我们可以创建一个 environment_mathlib 文件
里面如:
├── lean4:v4.23.0-rc2
├── lean4:v4.24.0
└── lean4:v4.24.0-rc1
这样 每个文件里面放的是对应的 .lake

我们在创建新库 C24.0 的时候就可以

```bash
ln -s path_environment_mathlib/lean4:v4.24.0/.lake/packages/ Cpath/.lake/ # 创建从A24.0 中.lake/packages/ 到 B24.0 .lake的一个 符号连接
```

