#How compile 8051_up

## Download duo-8051

git clone https://github.com/milkv-duo/duo-8051.git

## Download duo-examples

git clone https://github.com/milkv-duo/duo-examples.git

## Read the documentation and compile hello-word program

https://milkv.io/docs/duo/application-development/wiringx

## Copy the 8051_up source in the example directory

cp -a duo-8051/tools/8051_up duo-examples

cd duo-examples/8051_up

edit Makefile

change CFLAGS line

CFLAGS += -Isys_inc

make

if there are some errors with not defined environment assure you are running after source envsetup.sh 
