
import os
bazel_targets = []
with open("src/lib/dummytpl/BUILD", "r") as f:
    dummybuild = f.read()
with open("src/lib/dummytpl/DummyClassX.java", "r") as f:
    dummyclass = f.read()

for ii in range(0, 2):
    pkgname = "dummy" + str(ii)
    bazel_targets.append("//src/lib/dummypackages/" + pkgname)
    pkgdir = "src/lib/dummypackages/" + pkgname
    os.makedirs(pkgdir, exist_ok=True)
    with open(pkgdir + "/BUILD", "w") as f:
        f.write(dummybuild.replace("dummytpl", pkgname))
    for jj in range(0,3):
        classname = "DummyClassP"+str(ii) + "C" + str(jj)
        with open(pkgdir + "/" + classname + ".java", "w") as f:
            f.write(dummyclass.replace("dummytpl", pkgname).replace("DummyClassX", classname))


with open("src/masterlib/BUILD", "w") as f:
    f.write("java_library(\n")
    f.write("    name = \"masterlib\",\n")
    f.write("    srcs = glob([\"*.java\"]),\n")
    f.write("    visibility = [\"//visibility:public\"],\n")
    f.write("    deps = [\n")
    for tt in bazel_targets:
        f.write("        \"" + tt + "\",\n")
    f.write("    ],\n")
    f.write(")\n")




