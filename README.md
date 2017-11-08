numpy-wsgi-deadlock
===================

Build
-----

```
docker build -t numpy-wsgi-deadlock .
```

Run
---

```
docker run -p 8000:80 --name hello numpy-wsgi-deadlock
```

Reproduce
---------
```
curl http://localhost:8000/
```

Debug
-----

```
docker top hello
sudo gdb attach <pid-of-wsgi-process>
```

You will see the deadlock on thread 4:

```
Thread 4 (Thread 0x7fae53194700 (LWP 28580)):
#0  0x00007fae58dcc536 in futex_abstimed_wait_cancelable (private=0, abstime=0x0, expected=0, futex_word=0x55a7437040e0) at ../sysdeps/unix/sysv/linux/futex-internal.h:205
#1  do_futex_wait (sem=sem@entry=0x55a7437040e0, abstime=0x0) at sem_waitcommon.c:111
#2  0x00007fae58dcc5e4 in __new_sem_wait_slow (sem=0x55a7437040e0, abstime=0x0) at sem_waitcommon.c:181
#3  0x00007fae55064768 in PyThread_acquire_lock () from target:/usr/lib/x86_64-linux-gnu/libpython2.7.so.1.0
#4  0x00007fae54fd6556 in PyEval_RestoreThread () from target:/usr/lib/x86_64-linux-gnu/libpython2.7.so.1.0
#5  0x00007fae5508eb96 in PyGILState_Ensure () from target:/usr/lib/x86_64-linux-gnu/libpython2.7.so.1.0
#6  0x00007fae365764a6 in _error_handler (method=method@entry=0, errobj=errobj@entry=0x7fae49104758, errtype=errtype@entry=0x7fae365da9f1 "underflow", retstatus=retstatus@entry=4, first=first@entry=0x7fae53193890) at numpy/core/src/umath/ufunc_object.c:124
#7  0x00007fae3657bc6f in PyUFunc_handlefperr (errmask=521, errobj=0x7fae49104758, retstatus=retstatus@entry=4, first=first@entry=0x7fae53193890) at numpy/core/src/umath/ufunc_object.c:214
#8  0x00007fae36588de9 in double_power (a=0x7fae59753240, b=<optimized out>, modulo=0x7fae5547dd50 <_Py_NoneStruct>) at numpy/core/src/umath/scalarmath.c.src:1168
#9  0x00007fae55031a17 in ?? () from target:/usr/lib/x86_64-linux-gnu/libpython2.7.so.1.0
#10 0x00007fae54fd7e0a in PyEval_EvalFrameEx () from target:/usr/lib/x86_64-linux-gnu/libpython2.7.so.1.0
#11 0x00007fae5514615c in PyEval_EvalCodeEx () from target:/usr/lib/x86_64-linux-gnu/libpython2.7.so.1.0
#12 0x00007fae5509a5b0 in ?? () from target:/usr/lib/x86_64-linux-gnu/libpython2.7.so.1.0
#13 0x00007fae55032543 in PyObject_Call () from target:/usr/lib/x86_64-linux-gnu/libpython2.7.so.1.0
#14 0x00007fae55145587 in PyEval_CallObjectWithKeywords () from target:/usr/lib/x86_64-linux-gnu/libpython2.7.so.1.0
#15 0x00007fae5550c2d6 in ?? () from target:/usr/lib/apache2/modules/mod_wsgi.so
#16 0x00007fae5550fa7c in ?? () from target:/usr/lib/apache2/modules/mod_wsgi.so
#17 0x00007fae58dc4494 in start_thread (arg=0x7fae53194700) at pthread_create.c:333
#18 0x00007fae58b06aff in clone () at ../sysdeps/unix/sysv/linux/x86_64/clone.S:97
```

Cleanup
-------

```
docker kill hello
docker rm hello
```

