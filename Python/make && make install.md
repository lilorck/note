```python
/root/Python-3.6.7/Modules/_pickle.c:5818:9: warning: ‘s’ may be used uninitialized in this function [-Wmaybe-uninitialized]
     key = PyLong_FromString(s, NULL, 10);
         ^
/root/Python-3.6.7/Modules/_pickle.c:5808:11: note: ‘s’ was declared here
     char *s;
           ^
/root/Python-3.6.7/Modules/_pickle.c:4853:11: warning: ‘s’ may be used uninitialized in this function [-Wmaybe-uninitialized]
     value = PyLong_FromString(s, NULL, 0);
           ^
/root/Python-3.6.7/Modules/_pickle.c:4838:11: note: ‘s’ was declared here
     char *s;
           ^
```