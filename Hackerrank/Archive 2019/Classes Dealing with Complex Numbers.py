# import math
#
#
# # class Complex(object):
# # def __init__(self, real, imaginary):
# #     self.real = real
# #     self.imaginary = imaginary
# #
# # def __add__(self, no):
# #     a, b = str(no).split('+')
# #     b = b[:-1]
# #     a, b = float(a), float(b)
# #     res = (a+self.real, b+self.imaginary)
# #     return '%.2f' % res[0] + '+%.2fi' % res[1]
# #
# # def __sub__(self, no):
# #     a, b = str(no).split('+')
# #     b = b[:-1]
# #     a, b = float(a), float(b)
# #     res = complex(self.real, self.imaginary) - complex(a, b)
# #     if res.imag < 0:
# #         return '%.2f' % res.real + '%.2fi' % res.imag
# #     else:
# #         return '%.2f' % res.real + '+%.2fi' % res.imag
# #
# # def __mul__(self, no):
# #     a, b = str(no).split('+')
# #     b = b[:-1]
# #     a, b = float(a), float(b)
# #     res = complex(self.real, self.imaginary) * complex(a, b)
# #     return '%.2f' % res.real + '%.2fi' % res.imag
# #
# # def __truediv__(self, no):
# #     a, b = str(no).split('+')
# #     b = b[:-1]
# #     a, b = float(a), float(b)
# #     res = complex(self.real, self.imaginary) / complex(a, b)
# #     return '%.2f' % res.real + '%.2fi' % res.imag
# #
# def mod(self):
#     b = abs(complex(self.real, self.imaginary))
#     return '%.2f'%b+'+0.00i'
# #
# # def __str__(self):
# #     if self.imaginary == 0:
# #         result = "%.2f+0.00i" % (self.real)
# #     elif self.real == 0:
# #         if self.imaginary >= 0:
# #             result = "0.00+%.2fi" % (self.imaginary)
# #         else:
# #             result = "0.00-%.2fi" % (abs(self.imaginary))
# #     elif self.imaginary > 0:
# #         result = "%.2f+%.2fi" % (self.real, self.imaginary)
# #     else:
# #         result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
# #     return result
#
# class Complex(complex):
#     def __add__(self, no):
#         return Complex(complex.__add__(self, no))
#
#     def __sub__(self, no):
#         return Complex(complex.__sub__(self, no))
#
#     def __mul__(self, no):
#         return Complex(complex.__mul__(self, no))
#
    # def __truediv__(self, no):
    #     return Complex(complex.__truediv__(self, no))
#
#     def mod(self):
#         return Complex(complex.__abs__(self))
#
#     def __str__(self):
#         return '{0.real:.2f}{0.imag:+.2f}i'.format(self)
#
#
# if __name__ == '__main__':
#     c = map(float, input().split())
#     d = map(float, input().split())
#     x = Complex(*c)
#     y = Complex(*d)
#     print(*map(str, [ x + y, x - y, x * y, x / y, x.mod(), y.mod() ]), sep='\n')
# 2 1
# 5 6
import math


class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real+no.real, self.imaginary+no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        res = complex.__mul__(complex(self.real, self.imaginary), complex(no.real, no.imaginary))
        return Complex(res.real, res.imag)

    # def __truediv__(self, no):
    #     return Complex(self.real / no.real, self.imaginary / no.imaginary)
    def __truediv__(self, no):
        res = complex.__truediv__(complex(self.real, self.imaginary), complex(no.real, no.imaginary))
        return Complex(res.real, res.imag)

    def mod(self):
        b = abs(complex(self.real, self.imaginary))
        return '%.2f' % b + '+0.00i'


    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result



if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [ x + y, x - y, x * y, x / y, x.mod(), y.mod() ]), sep='\n')


