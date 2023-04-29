#include <stdio.h>
#include <stdlib.h>
#include <Python.h> 

int fab(int n) 
{ 
  if (n == 1 || n == 0) 
    return 1; 
  else 
    return n * fab(n - 1); 
} 

char *reverse(char *s)  
{  
    register char t,  
            *p = s,  
            *q = (s + (strlen(s) - 1));  
  
    while (s && (p < q))  
    {  
        t = *p;  
        *p++ = *q;  
        *q-- = t;  
    }  
    return(s);  
} 

PyObject* wrap_fab(PyObject* self, PyObject* args) 
{ 
  int n, result; 


  if (!PyArg_ParseTuple(args, "i:fab", &n)) 
           return NULL; 
  result = fab(n); 
  return Py_BuildValue("i", result); 
} 

PyObject* wrap_reverse(PyObject* self, PyObject* args)
{
   char* orig_str;
   char* dupe_str;
   PyObject* retVal;
   
   if(!PyArg_ParseTuple(args,"s:reverse",&orig_str))
	return NULL;
   dupe_str = reverse(strdup(orig_str));
   
   retVal = (PyObject*)Py_BuildValue("ss",orig_str,dupe_str);

   free(dupe_str);

return retVal;
}


static PyMethodDef exampleMethods[] = 
{ 
  {"fab", wrap_fab, METH_VARARGS, "Caculate N!"}, 
  {"reverse",wrap_reverse,METH_VARARGS,"reverse string"},
  {NULL, NULL} 
}; 


void initexample() 
{ 
  PyObject* m; 
  m = Py_InitModule("example", exampleMethods); 
} 