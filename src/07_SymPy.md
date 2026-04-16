---
prefix: 07_SymPy
source: 07_SymPy.ipynb
---

%% md hdr-01
<center>


<div style="display: flex; justify-content: center;">
    <img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAYEBQYFBAYGBQYHBwYIChAKCgkJChQODwwQFxQYGBcUFhYaHSUfGhsjHBYWICwgIyYnKSopGR8tMC0oMCUoKSj/wAALCAB1Aa4BAREA/8QAHQABAAIDAQEBAQAAAAAAAAAAAAcIBAUGAwEJAv/EAFMQAAEDBAADBAUFCQwIBgMBAAECAwQABQYRBxIhEzFBUQgUImFxMjeBkbEVGCNSdHWUsrMWMzZCVFVygpKh0tMkNENWc7TB0Rc1YoTh8CU4ZHb/2gAIAQEAAD8AtTSlKUpSlKUpSlKUpSlKUpSlKUpSlKUpSlKUpSlKUpSlKUpSlKUpSlKUpSlKUpSlKUpSlKUpSlKUpSlKUpSlKUpSlKUqvnpG8YMl4c5TbLfYWbcuNJhduoymVLVz86knRCh00BUS/fR55/JrF+iuf5lXStEsXC0wpiSCmQwh4FPceZIPT66j/wBIHOrpw9wZm82RqI7KXNbjlMpClI5VJWT0BB37I8arl99PnH8gsH6O7/mVZzghl9wznhzAv13bjNzH3HUKTHSUoAS4pI0CSe4eddFm94Vj+G3y8N9mXYMJ6QgODaSpKCUg+7YFVB++nzj+QWD9Hd/zKmf0b+K1/wCJUu/Iv0a3stwEMqbMRtaNlZXvfMo/i1ONVDzn0kcxsWZ320w4VkVGgznozSnGHCopQspGyHB10PKpn9HbiFduI2JXC531mG1IjzTGQIqFJSUhtCuoUo9dqNSrSlVd4zcfcqwriRdrBaolochxOy7NUhlxSzzNJUdkLA71Hwrs/Ru4rX3iW/f0X6Pb2RASwWvVG1I3zle98yj+KKme4vKj2+S83rnbaUtO+7YBNUq++jzz+TWL9Fc/zKffR55/JrF+iuf5lPvo88/k1i/RXP8AMp99Hnn8msX6K5/mU++jzz+TWL9Fc/zKffR55/JrF+iuf5lW64cXqVkeBWG83BLSZc6G2+6GkkIClDZ0CTofTXlxPv8ALxbh/fL3bkMrlwY5dbS8CUEgjvAIOvpqq0L0qcxRLZVMtdkdjBYLrbbTiFKTvqAorOjrx0fhVscFy605vjke82KQHYzo0tB6LZX4oWPBQ/8AkbBBroKUqCPSO4uX/htdrLGsMe3PNzGHHHDLbWsgpUANcqh51qfR/wCNuS8Qs6cs17i2tqKmG5ICozS0r5kqQB1KyNe0fCpf4tZFNxPh/dL1a0sqmRizyB5JUj2nkIOwCPBR8a66oUsGWcUMtuOSHGm8OZt9qu0i2J9fRJDiuzI0TyEjuI8uu+lTNF7b1Vn1rs/WOQdp2e+Xm111vrrdRXxj4rO4JkFjgQYaZiFf6ZdjyKUqNC50t840ehKldCdj2deNSsy6h5lDrK0rbWkKSpJ2FA9QRXH8Ts5bwu3Q0x4Lt0vdye9Wt1uaOlPue8+CRsbPvFcwJfGphr1523YZKSfaNtadeQ8B+KHCeTm/uqVoy1uR2lut9k4pIKkb3ynXUb91cZgOWzshyfNLdNZjNsWW4Jix1NJUFLSU72vZOz8NUu2WTofFuw4s0zGMCfAflOuKSrtApB6AHetfRXR5XcXbRi14uUZKFvw4b0htKwSkqQgqAOvDYrB4d3uRkuC2K9TkNNyp8RuQ4hoEIClDZABJOvpr0zMZObY3+4s2YXHtRz/dUOdl2ejvXZ9ebfL7tbqKcfyvi5fMkyKyRUYMiVY3GW5C3ESuRZcQVJ5NEnuHXYFTZbvW/ufF+6XYevdknt+w32faaHNy768u96311UV5dxbVYuLtsxpEVtyyAtR7nNKSTGkPhXYJ5t6A9kE78CfKpcqNeK2W5NZcmxGxYg1Z1TL4uSgruaXC2jskJUPkEEdCrwPhWpuubZ/gzTdxz2y2Sdj4WlEmbYnHeeIFHQWptzqpOyO6pcjPtSY7T8dxLjLqAtC0nYUkjYI92qrJ6blhW7bMcv7SCUMOOQ3iB3c4Ckfqr+uqlVe30Wc7Yynh5GtL7w+61lQmM42T1WyOjax7teyfen3isD0y/mlj/nRn9RyqQ1fX0UPmRs//ABpP7ZVc76XudsWbDBi0R4G53flLqUnq1HSrZJ8uZQCR5jmqllXO9C2wuQcCut4eRym5zOVv/wBTbQ1v+0pY+irDV+a/Fn50cu/O0r9qqrR+hP8ANxefzqr9i1VhaUqgHpQ/Pjkf/t/2DdSh6Df+tZh/Qi/a7VqpTKZMV5hZIS6goJHeARqq+feo4n/Pl9/tNf4Kfeo4n/Pl9/tNf4Kgn0hOG1s4aZBa4FomTJTcqKX1qlFJIPOU6HKB06VquBmEQeIOdosd0kyY0dUZx7tIxSF7TrQ9oEa6+VWL+9RxP+fL7/aa/wAFPvUcT/ny+/2mv8FTlidjYxrGrZZYjjrseAwmO2t3XMoJGgToAbrl+PnzN5Z+RK+0V+dNdzwk4kXbhvkaZ9uUXoLxCZkJStIfQPsUNnSvD3gkG/8AhWVWnM8ejXmwyA/DeGiD0W2sd6FjwUPL6RsEGt5SqienB/CLF/yV79dNc36G3zuPfmx79durMekV8zt/+Mb/AJlqpHquXC3h/b8tuOezZl0v0NxrJ5rIRb7guO2QCk7KR3q6nr8KsK2lq329CVukMRmgC46vZ5UjvUo+4bJqt+P2nOM+kZZltniY05aMnSuAym8KfDqYbZU2nkCBpIVrm+I3Ui+j7dpwxqZiV/Un7vYs/wCoPgK3zs62y4N/xSnoPcn31g8a1LxzN8FzmUw6/ZLO7IjTy2grMdL6AlLuh4A739HnXZSeJmEx7X90Xcqs3qvLzAplIUo+4IBKifdrddVFfblRWZDB5mnUBxB1rYI2KhrAb3bcW4tcRbVkU2PbZVwmtT4ZlLDSZDRQRtClaBIPQj4+R16NXWDlXpG2p/HpLVwiWazvImyY6gtptbitJRzjoVeOh7/I6kXiN832T/muV+yVXG8GsvxqNwvxOHJyKzsy0W9ltTDk1pK0q5QOUpKtg+6pTqJuFfzwcWvyqB+wVUkZJeIuPWC4Xe4K5YkJhb7h8SEjeh7z3D3mq2WbAuI2U4FeXHI+KhnLnRdXnJi3xLaJ0poApHKnlAHKPDZBqa+DGUvZXgcN+4bTeISlQLi2r5SJDXsq37z0V/WrluL82LbuLvCqXcJTESK29PK3n3A2hP4FI6qPQdSBX3jNxBx+bhVyxzH58W+3+9MqgxINvdS+oqcHLzHlJCQBs7PlUkYVanbFh1jtMhYcfgwWYziwdgqQgJJH0isTiLikbNsMulgmEJTLa024RvsnB1Qv6FAfEbFfnBkNnnY/e5tpuzCmJ0N0tOtnwI8R5g94PiCDWTiGTXXEL/GvFhlKjTWD0I6pWk96VDxSfEf9amPi7xvgcSOFse1SIDsC+tTWn3EJ9thaUpWCUq7x1UOhH0moCqwmA8eYuA8H4FhtEByZkCFPqK3hysM8ziiknrtZ0R0GvjUG5Fe7jkd5lXW9SnJc+SrncdWep8gB3AAdAB0ArKwrGbhmGTwLHaGyuVLcCd69ltP8Zav/AEpGyfhX6R4nYomMY3bbJbU6iwWEsoJ71aHVR95Oyfea2tfmvxZ+dHLvztK/aqq0foT/ADcXn86q/YtVYWlKoB6UPz45H/7f9g3Uoeg3/rWYf0Iv2u1a+lKp16bn8Nce/N6v2iq530QPnjZ/IX/sFXnpSuB4+fM3ln5Er7RX51p+UNjfWpf498HZXD+aLpaEOyMYlKHZuE8yoqj/ALNw+Xkrx7j17+c4P8TLrw2yES4ZVItj5CZsEq0l5PmPJY8D9B6E1f3D8mtWX4/FvNikpkQpCdg9ykK8UKHgoeIrc1UT04P4RYv+Svfrprm/Q2+dx782Pfrt1Zj0ivmdv/xjf8y1Uj1H8DP+HFnvE21w71ZbfPdmLMppOmeaRvlWVnQBVsaJJ8K7qVHYmxHY8ppt+M+gocbWApK0kaII8QRXP33JcVwGBb412mwrLDWktRWuXkRpAGwkJGgBsfXWNh2RYXlF4uE/FZVtm3MNoTLkR29OlHXkC1aBI6HXwrrXkIcaWh5KVtKSQpKhsEHvBHlUNu3rgZasgUD+5Fq5IX1W3EQpKFePtBJSD9NS9b5kW4QmZdukMyYjqQpp5lYWhafMEdCK5rKm8PveQW/G8mgwLhc5DK5MViVF7X2E/KUFFJCfrBre2OyWuwwhEsluiW+LvfZRWUtpJ8yAOp99czlvEfBbJIftGSX63IdWktvxV7d9kjRStKQdbB7jXjj2IcNb3CZudgx/F5sYq2iRGhsqAUPeB0I8u8V1l/vNux+0v3O9S24cBjl7R9w+ynagkb+kgfTX22QbY29IuVsjxEu3EIdelMITuSAPYUpQ+V0PQ+RrCRJsGYQ7nbz6ndosaQYk2O4gOIS6gglCkkaJB0a3aEJbQlCEhKEjQSBoAeVaDEpWN3BV1mYsYDilTFtTnYiAkrkJ+VzkAcyuo6+O6yr/AI1Y8iDIv9nt9zDG+yEuOh3k3reuYHW9D6q1WDQcMSmZIwu32djsH1xJDkGKhopdTrmQSAD02K6ulQ/x84NROIsEXC2KaiZLGRytuq6IkJHc25/0V4fDuo/klguuM3Z62X6C/BnNfKadTrY8we4g+BGwa1dKVvMPxW9ZheG7Zj0B2ZKWRvlHstj8Zau5I95q9PA7hLA4aWha1rRMv0pIEqWB0SO/s299QkHx7yep8AJPpX5r8WfnRy787Sv2qqtH6E/zcXn86q/YtVYWlKoB6UPz45H/AO3/AGDdSh6Df+tZh/Qi/a7Vr6UqnXpufw1x783q/aKrnfRA+eNn8hf+wVeelK4Hj58zeWfkSvtFfnUn5Q+NfqLMt0O7WZyBcozUqFIZ7N1l1O0rSR1BFUY4+8HpfDq6GfbQ5JxmUvTLx6qjqP8AsnD9ivH41ouDfE+6cNcg9Yjc0m0yCBMhFWg4n8ZPkseB+g9Kv3imR2vK7DFvFilIkwZCdpUO9J8UqHgodxFVb9OD+EWL/kr366a5v0Nvnce/Nj367dWY9Ir5nb/8Y3/MtVI9U7uN/MDFuJtqexUz4twyWbHF5f5fVoTjikpClnRUkp6KB7tkVanB7cu0YZYrc7MTNXEgssmSk7S7yoA5gfEHXT3VF/HyS9DzvhnIjWld4eRLmFMFspCnvwSegKunTv6+Vd1w+us25qnev4Y/jPZhHIXVNK7ffNvXJ5aHf+NXN+kjPlRsEhW+LJciNXi6xrZKkNnRbYcJ5zvw2E6PuJreXhnEuHOIR2FWLdoChGDESAZKiSknmWACT0SdqPj399bXhxcbDdsMt03EWEx7G4F+rNJZ7IJAcUFaR4DmCq4vJP8A9k8P/M0v7a6/ipdpdi4cZJdLaSmbFguuNKA3yK5eivo7/orQ8GMMsFp4e2d+PDjS5dxiNy5c11AcckOOJClFSjskbPQf9d1zkG2xcL9IuFb8aQmLbshtjsidAa6NIdbJ5XgkdE70U9OnU+dbj0nfmQyT4Mft260eMzZPB/IImN3uQ69g10Xqz3B5WzAdV19WdV+KevKo/wDfl3HAgauHEkH/AHrmfYit3xvzAYTw3utzacCJziPVYezr8Mvok/1RtX9Woc4J3jHcJ4jwMdsF/jXS2X+3th9TTpUG7i0PaPXuSsb179Dwqz1RN6OX/kWX/wD+on/aipZqCeP3Gq7cNMnt9sttrgzGpMMSVLkKWFBXOpOhojp7IqMPvsMk/wB3rR/ac/xVo8r9IN3LoIh5JhWPXBgdU9r2vMj3pUFcyT7wRUM3eRDlTVu2+D6iwruYDqnAn4FXX691hVsrHMgQpgeudsTc2R/sFvraSfiU9fqIqZ8b9I2XjFuTBx/Dcet8UdeRgOJ5j5qO9qPvOzW2++wyT/d60f2nP8VS56PnF658Tpt6ZuduhQ0wG2loMcqJVzlQO+Yn8Wppr83+NLBj8WsvQoa3dH1ge5Syof3GrI+hHKQvCshiBQ7Rq4JdI8gttIH6h+qrH0pX57+klKTL425QtCgpKHm2unmlpCT/AHg1MfoOR1CPl8kj2SuK2DrvIDpP2irS0pVOvTc/hrj35vV+0VXO+iB88bP5C/8AYKvPSlcDx8+ZvLPyJX2ivzqT8ofGv1Pj/wCrtf0R9leF3tkK82yTbrpGalQZKC26y4NpWk//AHv8Kohx54QTeHF29agh2VjUpf8Ao8kjZZUf9k57/I/xh79gavgtxSufDW/dq1zybLJUBNhb6KH46PJYH19x8x3/AKXN+tuTuYXeLJJTJt8qE8ptxP8ATSCkjwIPQjwNa/0Nvnce/Nj367dWY9Ir5nb/APGN/wAy1Uj1wOE8PkWe2Zhb705HuEPILpKnKaCCAGngByK34jXeKzeFuMXTDsdVY7jcm7jBiOqTbneUh1Efe0tueBKe4EeHTwrXcUcMveSXnF7tjdzgwJ1kdedSZbKnUqLiUp7gfAA/XW2wqFmcWTKOYXe0z2FIAYTCiqZKVb6kkk7Gq2OaYxbcxxqZY702pcOSnRKDpaFA7StJ8FAgH/4rgI+LcVLdB+5ULM7LMgpSW25k+Aoyko7hvSuVRA8T1NdlwyxMYPg9rx1MwzfUkrBfLfJzlS1LPs7Ovla7/CvO5Yf67xKs+Weu8n3PhPRPVey32nOd83Nvpry0a6abFYnQ34ktpD0Z9tTTraxtK0qGiCPIg1Ett4fZzhza7dgeWQTYOcqYh3iKp1UQE7KULSdqHXoD/wDJ6Ph9w+Xj94n5FkF1dvuUz0Bp2c42G0NNA77JpA6JTsD46HdWfxZxR/N8AumPRJTUV6Z2fK86kqSnlcSs7A69ydVt8jx23ZLjkmyXuOmTBkNdm4k9/uUk+BB6g+BFcpwX4fSOHdnu9vk3P7pCXcFym3lJIXyFCUgL33q9nrWZlmFvZNnWN3O4SWFWOzBx8QSgkvSVDSVq8NJHUe/fnX88SsBjZVjYi2v1a2XeNIamQZqGQCw82rYPTrrWx9PurtIvbCMz60WzI5B2hb3y82uut9dbqHbBgPEPF3bw1jmS2FqDPuL9w5JEFbi0qcO9b2PACpas6JzVqiIuzzL9wS0kSHWUFCFua9opB7hvwqn/AKbPzh2T81J/bOVXelKUpSrP+g7/AObZb/wI36zlW1qlfpgYU/Z85Rk0dom3XdKQ4sDoiQhOik+XMkBQ8/a8q4TgjxNk8M8nXMDKpVrlpDUyMk6UpIOwtPhzJ2db6EEjpvYu3iPFHDcritu2m/wu1UNmNIcDLyT5FCtH6Rse+umkXi2Rmi7IuMNpsd61vpSB9JNRDxS9ITGMXgPx8dlM3y9EFLaY6uZhpX4y3B0IHkkkn3d9UguU6Tc7jKnTnVPS5TqnnnFd61qOyT8Savr6NGFPYZwyiouDRauVyWZshChpTfMAEIPkQkAkeBJqVqUqnXpufw1x783q/aKrnfRA+eNn8hf+wVeelK4Hj58zeWfkSvtFfnUn5Q+NfqfH/wBXa/oj7K9Kwb5aYN9tEq2XaM3KgykFt1lwbCh/0PiCOoI2Kobx14ST+G95L0cOSsclLIiyiNlB7+yc8lDwPcoDY8QIuLi1NpbK1FtJJSknoCe/Q+gfVU5eht87j35se/XbqzHpFfM7f/jG/wCZaqR6r7w54tXaLlt3h52+j9z8q7yoNtuiwlCI7rSv3hwgAAFJSUk9d76nrr3sfE+/ZPxpx1m3BUXBp/rjMQqbTzTyy2Sp7qOYJ5iAnWu4767AnuoKgu5jlmfZtEh5+7YYNonIjsR0wWHgUqRvvVo/bUx43FlwbHEjXK5qu0ttGnJqmktl47J3yp6DpodPKo046ZZlWNXzDGsNbEt+Y9JL8ApSfW0NtpWUbI2Drm1rrvXf3V08bN4eS8LblkuNyClSID7iQoDtI7yGyShafBSTrp3HoeoNZvCu5zL1w4xu5XN4vzpUFp550pA51lIJOhofVXC55Nyq6carfimP5Q9YYTllM9am4jT/ADLDqk9yx4jXj4V5Xm85vwukwbhlF8YyjEn5CI0uQqGmNJhFZ0lzSPZUnffvr3CpoBBGx3VClru2acVbjcZmM31GL4hEkrix5DcZL8mcpB0pftdEo33a+HXrrJi37LuHmX2a0ZrdGsgx69PiHEuvq6WH48g/JbcSnoQruB7+8+GqmFQJSQDokdD5VCub2zKcOxqbfLxxYuKIkZOwhNpi87ij8lCenVRPQfX3V1fBWLlyMRbnZ9dHpl1naeTHW0hv1VvXspISke0d7O+7oPA76/JLxFx6wXC73BXLEhMLfcPiQkb0Pee4e81FfAPOcgvky52fOAG7u603eIIICeaG8NhIAA6IOh16+1o91TLWNKgQ5awuVEjvLA0FONhRA8uorTZK7jGM2aRdb4zbYcBgbW64yn6ABrZJ8AOpqonE7j/Ku8l2JhNsiWa2glIkqjNqkujz7iEfAbPvqDZUh6XIcfkurdecPMtazsqPvNeVZECbJt8tuVBfcYkNnaHG1aINT7wt9IP1GQ1Bz+1Q7jCUQn7oMxUJfb960gaWPho/GraWdnHrzbI1xtUe2y4MhAW0800gpWPq/u8K2cWFFiFRixmGCr5RbbCd/HVZFarKMftmUWOVaL5FRKgSU8q21eHkoHvBB6gjqKqDxI9GfI7LIdk4gsXu272lkqCJLY8iDoL+I6nyqFLvjd8szqmrtZ7jCWk6IkRlo+0VrUNOOK5W21qV3aSkk11uMcM8zyZ1CLPjtwcQoj8M40Wmh/XXpP8AfVneDPo5w8YmR71mLzNyurJDjMRsbYYV4KJPy1Dw6AA+fQ1YalKVUf0zbTcrjmVhXb7fMlITAIUphhSwD2iuhIFc/wCibZbrA4uMvTrZOjM+pPjtHo60J3odNkaq7FKVwvHRh2TwiylmM0488uGoJbbSVKUdjoAO+vz+TjF+5h/+Eunf/JHP+1fpxH6MN7/FH2V/dK1+Q2W3ZFZpVqvMVuXAko5HWljoR5jyI7wR1B61RHjDwZveC5CW7dFl3OyySVRJLLRWpI/EcCR0UPPuPePEDr/REs10gcVnnp9tmxmjbXk87zC0J3zt9NkVYj0ivmcv/wAY3/MtVI9Qhwjxm2ZXg+b2fIIYkQZGTziUK2kghSCFJPeCPMVn5VAYt/HLhVEgR0sQ40S4NNttp0htIZAAHlUwVVOQeGTfFPiD/wCJsdK5CrigxCtqQr2OT2tdkNd+u+rHYHIscnELW5ievuEGuSIAladISSnWl+13g99cVxPSo8WuFJCSQJc7ZA7vwArnOLuL3TDTf8swqOp+3XSK6zfrSjoF8yFJEpseC072rQ6jZ8SakHgoCnhJiIUCCLazsH+iKj3PsntOIekfa7rkMlcWAccUz2oZW4OcvqIGkgnwNeefZO3xlt7GHYPEnSbdLktLud2ejLZYjsIWFkJKwCpZIGhr/uJ5QhKWw2B7IHKB7qgTAcojcGmZmH52zKg25mW69bLulhbkeQytRUAopBKVgk7Hv+BPveb1/wCMmW4zBxaLLXi1muDd1m3d5lTTbq298jTXMAVE7O+njvw6zqtSUIUtaglCRsqJ0APOqw3HibiWX8Ukzsruhj4rjzm7XDMZ1wTpHjIWEpI5U69kH3HxUKnXCeIGNZu5LRjNwVMVECVPAx3GuUK3r5aRv5J7q4jjw3Ly64WDhza31R13dwzLhICOcMRWuo2O48ywNDzTrxrm85xbJ8EuVl4gzcnfyIWV1EeSwLc1HUITh5XNdn8rWwQCOnf01VgY7zcmO0+wsLZdSFoWO5SSNgikl9qLGdkSXEtMNILjjizpKUgbJJ8gK/P7jzxQl8RsoX2DjjePw1lEGOegUO4uqH4yv7h08yYwropWF5BDxNGSzLY/GsrjqWWpDw5O1UoEjlSepGknqBr31ztdC5hmQIxKNkwtj7lifK0iW0AtKClRSefXVHUd50DXPVMvo48V38DyJu13V9SsZnuBLyVHpGcPQOp8h3cw8R17wKvekhQBSQQeoI8aUpQgEaI2K/hLLSFbS2hJ8wkCv7pSlKUpSlKUpSlKUr4tKVpKVpCknwI3X2gAHcNU0N711pXwpSTspG/hX0AAaA0KaBI6d1KAaGh3V8KQe8A19pXxSUrSUrAUk94I3X0AAAAAAeAoRsaPdXzkT+Kn6qAAdwA+FfdDe9DfnQ9Ro91B0Gh3VBvpd5Y5YOGyLVFcKJN6e9XUQdHsUjmc+v2Un3KNUdqyPorcI4uRE5dk0ZL9tYcKIMVwbQ+4n5Tih4pSegHcSDvu0ZM9MoBPCOMEgAC6MgAf8NyqRVfP0VW0PcDbU06hLja3ZKVIUNhQLq9gjxFQL6T/AAlYwq5M3/HmezsM9woWwkdIr2idDyQoAkDwII7tVA1X79GHLHMq4UwBKcLk21rMB1RPVQQAUE/1Ckb8walhaghClKOkpGyT4Cta1f7U9jpvzc5lVnDCpJlg+x2QBJVvyABr5KyC0xEWxcm4R2kXNaW4alr0H1KTzJSnzJHdWRNukKDLgxZcltmROcLUZtR6urCSoge/QJ+ivL7t231y4xPXGjJtzSXpbYO1MoUCUkj3hKvqrzfyOzx8cF/euMZFlLSXxMK/wZQrXKd+/Y+usHJs3xrF347GQXiNAefQXGkOk7UkHWwAK9LlmWPWzH4l8uF2jR7TLKQxJWSEuFQJSB031AJ+is+xXq23+2NXGyzo86C5vleYWFJJHeNjxHlWtsGb4zkN1kW2yXqHNnMJK1tMr2eUHlKge5QBIGxsdazW8itDtvuc5u4MKiWxx1qY6Feywtrq4FeRT41p7HxJw2+3BuDasjt0iY7+9sh3lU57kg65j8K6C9XWDZLXIuV2lNxIMdPM684dJQN66/SRWSp9pMYyC4nsAjtC5vpy63vflquStHE7CbvPZhW7Jba7KePK032vKXD5J5tbPuFdjXDSeLWCRpDkd/JoCHm1FCkEq2CDoju8NVtrznGNWW12+43W8RYsK4JCorrhOngQFbT033EGthZL9a75aE3S0zWZNuVzakJOk+ySFdT5aNaO18TMLut3btduyW2yJzi+zbbQ7++K8kK7lH4E10Dd4tzl7ds6JrBujTIkLi834QNk6C9eWxrdf2zdIT91k21qS2ufGbQ68wD7SEL3yk/HlP1Vz2QcR8Px66G3XnIYEWaNc7Sl7Le+7n1vk/rarfy7xbollcu781hNsba7dUoLCm+z1vm5h3jXjWY04h1pDjagpCwFJUO4g9xrg8u4n4/j+R2+0PXi0tOqdInqfka9VRy9AQAdKUopA5tADZPhvu2Xmn2G32HEOMuJC0OIUClSSNggjoRrxrkmOJuFSLum2M5LbVzFO9ilId9lTm9coX8knfTQNdI7dITV2YtjkltNwfaW80wT7S0JIClD3AqH11qcpzfGsUdZayG9Q4Lzw5m2nF7WoefKNnXv1qtpZLvbr7bGbhZpsedBd3yPsLC0q0dHqPEEEar5bbxb7nInMW+YzIegveryUNq2WnNA8qvfois+sC03m3XgzBa5rEow5C4sgNK2WnU/KQoeBFf3a7nCurTzluktyEMvLjOKQd8riFcq0n3gjVfzbrxb7lKnxoExmQ/Ad7CShCtlpegeVXv0a1+U5hj2KIZVkV3iQC9+9IdX7a/PlSOpHvAr+oGXY/cMcfv0G7w5FnYSpTsptzmQ2EjaubyIBB0etZ8+7W+32ld0nzY8a3IQHVSHlhCAk9x2fPYrS4vn2K5VKcjY/fIc2ShPMWUK5V8v4wSdEj3jpW4N5tqb6myqmsC6qj+tCKVacLXNy84HiNgiv7TdISru5akyWzcW2EyVR9+0G1KKQr4EpI+iv5fvFvYvMa0vTGUXKS2t5mOVe2tCNcxA92x/9Br+p90hW9+EzNktsuzXuwjpWdF1zlKuUe/SSforMqnnpuzFrzLHYRP4NmAp4D3rcIP7MVW6v0z4d2dqwYJYLXHSEojQmkHXirlBUfpUSfpqKfTL+aWN+dGf2btUiq+voofMjZ/+NJ/bKrpeOdnavnCTKYryQeSE5JQT4LaHaJP1pr85atV6Dk1e8ugk/gx6s8keR/CA/YPqq0stCnIryEdVKQQPjqoBteU2OL6M0iySbpEZvTVofti7ctwCSJXKpsNdl8rmKiPD391b/iBj0a7weFtgvsdRZdkdg+3zFKkqEF3qCO5SVAEHzArUybjeYXEnAMVyntZM+DcXnYl05PYuEX1V1IWo+DqSQlafeCO+u1xPR418QB//ABWz9V6uKttnnfu5j8NHGFjHLXcFZCl3+IuGVc7EfXiEyCrof4rYrZcSrhJt3GeyvQ79ZrE6bFISZN2QFNKHbt+wBzo9o6339wPSsviq/Nm4zw9dg3S2ybk7kEPspzbfPFcd7N32wkL2Ub30Cvpr24OdnAg5haMgPZ5Gi4vTbu0gcraw6kcrrAHXslISNfxuYK31rA4VXli2ZNbcStd4tmS2E25yRbJscpMmC0lSB2L/AC9NEKACuhJSQR06Y1tIPCnjJog6ud8/UNYuW5DjF44I2uyw50C65I9bozNthwnkOykSwhHIpISeZBSobKumgDutpxaXc8guOPYbEtSb8tltF1vUQSUx0Oto9ltClka0p32ta2Q3WdwtuU5PD684xf0KYvmOsriPNLdDiuwU2VML5h0UOQhO/EoNcqjJcQlejna7LOnW65XRyytR41tYcS9KMrswGwltO1JWF6666a3U24ozPj4vZ2bwvtLm3DZRKXvfM6EALO/H2t1x+UfPbgn5vuf2MVpOOMp2Fl3DuRGulutLyJkvlmXFPMw1uMoe0OZPfvQ9odSK9eIK7heuCspYuUPIPwzapztlTpD8VL6S8hAC1dezBBHN10fPVdLbcywCVEtEa3XmwutOuNNwIrLjZUFkgICWh1SQdeA17q4zIsYdyDjDkUq0y/UMitlrgP22Z1KULK5AU2sD5Tax7Kh5dfCvXhTf38h4p5hImQHbbdGLdAjTIjo/eX0qf5gk/wAZB2FJUO8EV4cHsgxfHcJlWzKp9ttmRsSH/u41cHENuvvFaiXDzaLiVJIII2CNCtXDYW16OOeussOxrNJVcZFoYdSUFuEo7bASeqUk8ygPJQqWcXyKz3m1MxbHerZNmtxEqLceUh1SPZA2pKSSBsio74R5HiGP8PFWvJJ9ttl6jKdTe41xcQh9yQVErUsK6uBW9gjYIIA8qwLdbb076OeTMWOPLZblOy3rTF5Sl5NvU9zJbCT1BLfPyjyUK2V+4i2G14tjpws4xOs63mI6rc9I5JDXM4hKA2wATzJ2SoK0Ry7610d6+fbGPzLO/aMVpMMu9lxziBnDeXzIdvyCVcC/HkznEtdvAKEhlLa1aBSnSgUg9DvddVds0sNp4f3TJLE7EmQWO07L1TRRIkFXKEJKeiipwgbG97qK+HETIOHeXWh/JbMbdDvw+59ylmeiQJNwUtbrbygkewVFS2/EdUDw62IqAMTtNztkjJszxNtcm4MZBcWLlbUq6XGMl9RASO4PI2Sg+Oyk73W44dZjBtHCPKcrRzrifda4yo7a0lK3St9XZI13hSlKSnXma5zh3FyHh9ltom5NZlW+Lfv9AukwzkPiTPcWt1p5SUj2NqUtvxGlJHh1662XKz49xly17MJMWDcJqI6rTLnLCG1xEtgKbaWroCHOYqTsE7B61sOIl2sV54O53IxuVClsJhyUPvQylSFPBob2pPRR0U9evhWs4kFiPF4cXG+NlzFIUlLly2nnbbUWClhxwfiJcPUnoNiv44iXqw5LkGFxcSmwrnkrN2YktO291LpjRUn8Opxad8rZRtPKT7RI0DXnm+M/um40PIiTFW+8wMeYl26cjqY7wkujZH8ZChtKknvBNf3w5vsu+cYryq8QF268QrFHhz45+QHUvuq5m1fxm1JUlST5H3VxF8dyXIb9cOI9hsC50W3y0uWqemchH+hRi4l5CWtcyg9t49+ztOu7rInEi/2uQ5wxvvr0dq0v3hEhMl5wIQEKivEEknQ7x31JNou1uvMUybPcIk+MFFBdivJdQFDRI2kkb6jp76/uXb4UxYXLhx31gaCnWkqIHl1FeP3EtP8ANkH9HR/2rYAAAADQFYtxt0K5xwxcocaWwFBQbkNJcTsdx0QRvqa1v7kMa/3es/6E1/hraQIUW3xkxoEZiLHSSUtMNhCRs7OgOleziEOtqbcSlaFApUlQ2CD3gitb+52yfzPbv0VH/asqDbYMArMGFGjFegostJRza89CsqsBVmta7kLiu2wlXAd0osJLo/r63/fWW7HZecaW602tbSuZtSkglB1rYPgdEj6a+OxmHnWXHmW3HGSVNqUkEoJGiUnwOunSiI7Lch19DLaX3QA44EgKWB3AnvOtnXxr++zR2pc5E9oRylWuuvLfl1NYdxs9sua0KuVuhzFIGkmQwlwpHu2DqvVFvhIYjsIiR0sx1BTLYaSEtEdxSNaBGz3V6eqxxLMrsGvWijsy9yDn5N75ebv1vrqvCDarfb3X3YECJFdfPM6tllKC4fNRA6n416phRUsvtJjMBp8qU6gNjlcKvlFQ8SfHffWNb7Jara6p23WyDEcUNFbEdDZI+IFZaI7CJDj6GW0vuAJW4EgKUB3AnvOtn66+eqx+3de7BrtnUhDjnIOZaRvQJ8R1PT31iQLFaLe/28C1wIr2tdoxHQhWviButjXkuOyuQ2+tltT7YKUOFIKkg62Ae8b0PqrxuNsgXNCEXKFFloQdpTIaS4EnzGwa9IMKLb44jwIzEVgEkNsthCQT39B0rFjWK0RZypsa1QGZi+qn246EuH4qA3WamOymQt9LTYfWkJU4EjmUBvQJ7yBs/XXxEZhEhyQhltL7gCVuBIClAdwJ7yBs/XWLPstruElqRPtsKVIa/e3XmELUj4EjYrLkMNSWFsyGkOsrHKttaQpKh5EHvFYdustqtjqnbbbIMR1SeVS2GENkjv0SAOnSvs2y2qdLblzbZBkSmvkPPMIWtHwURsVn1rk2K0JuRuCbVAE8nZkiOjtSfPn1v++sxUdlUlEhTLZfQkoS4UjmSk62Ae8A6H1Vj3S0267NobutviTUIO0pkspcCT5gKB1Xp6hD9Waj+qR/V2iFNtdmOVBB2CBrQIPdXpJjsSmw3JZbebCgoJcSFDYOwdHxBG69a82I7McLEdptoLWXFBCQnmUepUdd5PnXibdCLJZMON2Rc7Yo7JPKV75ufWvlb677916yY7Eprs5LLbzewrlcSFDYOwdHxBANeNytkC6MBm5wosxkHYbkNJcTvz0oGvrdvhNwDBbhx0QikoMdLSQ3ynvHLrWqyC02Wi0UJLRTylBHTXdrXlWHbLRbbUHBa7fDhBw7WIzCW+Y+/lA3WV6uyJJkBpv1go7Mu8o5ine+XffrZ3qvnqzBkLfLLXbrQG1Ocg5lJGzyk9+up6e+vseOzGjojxmW2mEJ5UttpCUpHkAOgFYj9mtkiE1DkW2E7EaO22FsJUhHwSRod5r2t9vh21gs26JHiMlXMW2G0tp356A7+grJpSlKUpSlKUpSlKUpSlKUpSlKUpSlKUpSlKUpSlKUpSlKUpSlKUpSlKUpSlKUpSlKUpSlKUpSlKUpSlKUpSlKUpSlKV//2Q==" alt="Logo UTN"/>
</div>
</center>
<center>
    <div style="font-family: 'Georgia', serif; font-size: 24px;">
        <p><strong>Ingeniería en Electrónica. Análisis de Señales y Sistemas</strong></p>
    </div>
</center>

%% md prov-01
#Introducción a SymPy


# 1. ¿Qué es SymPy?

SymPy es una biblioteca de Python para matemáticas simbólicas. Esto significa que, a diferencia de las matemáticas numéricas donde trabajamos con valores específicos, en las matemáticas simbólicas trabajamos con símbolos y expresiones algebraicas. SymPy nos permite realizar cálculos matemáticos complejos de manera simbólica, lo que es muy útil para resolver problemas de álgebra, cálculo, y análisis matemático de manera exacta.

# 2. Importación de SymPy

La importación de SymPy es un paso necesario para poder utilizar sus funcionalidades. En Python, usamos la palabra clave `import` seguida del nombre de la biblioteca. Aquí, `sy` es el alias que usamaremos para abreviar SymPy.



%% code prov-02
import sympy as sy

%% md prov-03
Adicionalmente dentro del entorno de Jupyter podemos ejecutar la siguiente instrucción que permite *renderizar* las expresiones resultantes. Esto es para que se muestren las ecuaciones con un formato más agradable.

%% code prov-04
sy.init_printing()

%% md prov-05
Ahora podremos usar la función display() para que las expresiones aparezcan renderizadas.

%% md prov-06
# 3. Variables simbólicas

Las variables simbólicas son el elemento fundamental de `SymPy`, ya que todas las operaciones de álgebra simbólica dependen de ellas. Para crear una variable simbólica, utilizamos la función `symbols`, que asigna un símbolo específico a dicha variable:

%% code prov-07
x = sy.symbols("x")
print(type(x))

%% md prov-08
Con la función `symbols`, se define una nueva variable simbólica que se almacena en `x`. Al hacer esto, se verifica que `x` es un objeto de la clase `Symbol`. Una vez que la variable x está definida, se pueden empezar a crear expresiones algebraicas y manipularlas matemáticamente. Por ejemplo, podemos sumar, restar, multiplicar y dividir usando `x` como si fuera cualquier otra variable matemática, pero con la ventaja de que `SymPy` nos permite realizar estas operaciones de manera simbólica y no numérica. Esto significa que podemos simplificar, expandir y factorizar expresiones, entre otras operaciones.

%% code prov-09
x + 2

%% code prov-10
x**2 - 2*x - 10

%% code prov-11
sy.sqrt(x) - sy.sin(x)

%% md prov-12
Puedes definir múltiples variables separando por comas cada representación simbólica. Por ejemplo, si deseas definir las variables `p`, `q`y `r`, puedes hacerlo de la siguiente manera:

%% code prov-13
p,q,r = sy.symbols("p,q,r")
p**q + r/q

%% md prov-14
## 3.1 Variables simbólicas con restricciones

Cuando trabajamos en un contexto específico, como en ecuaciones donde necesitamos números enteros o valores reales, es importante poder restringir nuestras variables simbólicas. En `SymPy`, podemos definir variables como enteras (`integer=True`), reales (`real=True`), o complejas (`complex=True`). Al declarar estas restricciones, le indicamos a `SymPy` cómo debe tratar a cada variable durante los cálculos.

Por ejemplo, si definimos una variable `n` como entera y `y` como real:


%% code prov-15
n = sy.symbols('n', integer=True)
y = sy.symbols('y', real=True)

%% md prov-16
Este tipo de restricciones en las variables es útil en muchos contextos, ya que ayuda a SymPy a realizar los cálculos de manera coherente y evita ambigüedades en expresiones simbólicas.





%% md prov-17
# 4. Simplificación y expanción de expresiones:

SymPy es una herramienta muy poderosa para la manipulación y simplificación de expresiones algebraicas. En los siguientes apartados, revisaremos algunos casos básicos y explicaremos cómo utilizar las diferentes funciones que SymPy ofrece.

Para comenzar, es necesario definir algunas variables simbólicas que utilizaremos en nuestros ejemplos.



%% code prov-18
x,y,z = sy.symbols("x,y,z")
a,b,c,d,k,m,n = sy.symbols("a,b,c,d,k,m,n")

%% md prov-19
Por defecto, SymPy evalúa y simplifica automáticamente las expresiones algebraicas combinando términos semejantes. Observa los siguientes ejemplos:

%% code prov-20
x**2 + 5*x**3 - 10*x**2 - 5*x - 10*(x + 1)

%% code prov-21
expr = a*b + c*d + x/y - 7*a*b
expr

%% md prov-22
## 4.1 Factorización de Expresiones

La factorización es una técnica que nos permite expresar una expresión algebraica como el producto de sus factores. Esto puede ser útil para simplificar expresiones complejas, resolver ecuaciones, o reescribir términos. SymPy ofrece la función `factor` para factorizar expresiones de manera automática.

Por ejemplo, si tenemos la expresión $ ab + ac$, es fácil identificar que se puede factorizar como $ a(b + c) $. `SymPy` realiza esta factorización sin ningún problema:


%% code prov-23
expr = a*b + a*c
sy.factor(expr)

%% md prov-24
De igual forma se sabe que una expresión de la forma $ ac + ad + bc + bd $ se puede factorizar como
$ (a + b) (d + c) $.

%% code prov-25
expr = a*c + a*d + b*c + b*d
sy.factor(expr)

%% md prov-26
Otro ejemplo común es el de un binomio al cuadrado. Sabemos que $ (a+b)(a+b) $ puede factorizarse como $ a^2 + 2ab + b^2 $.


%% code prov-27
expr = a**2 + 2*a*b + b**2
sy.factor(expr)

%% md prov-28
## 4.2 Expansión de Expresiones

La expansión es el proceso inverso de la factorización. En lugar de encontrar factores, expandimos una expresión algebraica al multiplicar todos sus términos. `SymPy` ofrece la función expand para obtener la expresión expandida de cualquier producto.

Por ejemplo, si tenemos una expresión factorizada como $(x-7)(x-3)$ la función `expand` devolverá la expresión resultante de realizar la multiplicación:

%% code prov-29
expr = (x-7)*(x-3)
sy.expand(expr)

%% md prov-30
`SymPy` también puede manejar cualquier cantidad de factores. Aquí mostramos algunos ejemplos con diferentes combinaciones:

%% code prov-31
expr = (x + y)*(x - y)
sy.expand(expr)

%% code prov-32
expr = (x + y)*(x+y)
sy.expand(expr)

%% code prov-33
sy.expand( (x + y)**2 )

%% code prov-34
sy.expand( (x + y)**3 )

%% code prov-35
sy.expand( a*(m + n)**2 )

%% md prov-36
## 4.3 Simplificaciones

Para simplificaciones y operaciones más complejas, `SymPy` ofrece una función general llamada `simplify`. Esta función evalúa y simplifica una expresión utilizando varias técnicas según el contexto y el tipo de términos involucrados.



Suponiendo que se tiene la siguiente expresión algebraica racional y se requiere reducir:

$$ \frac{x^2 - 3x}{x^2 + 3x}$$

Se puede notar que tanto en el numerador como en el denominador se puede factorizar $x$, lo cual conduce a:

$$ \frac{x(x - 3)}{x(x + 3)} = \frac{x-3}{x+3} $$

Con `SymPy`:

%% code prov-37
expr = (x**2 - 3*x)/(x**2 + 3*x)
sy.simplify(expr)

%% md prov-38
Más ejemplos:

%% code prov-39
sy.simplify( sy.sin(x)**2 + sy.cos(x)**2 )

%% code prov-40
sy.simplify( sy.cos(x)*sy.cos(y) - sy.sin(x)*sy.sin(y) )

%% code prov-41
sy.simplify( (1+sy.tan(x)**2)/(1+sy.cot(x)**2) )

%% md prov-42
Para la manipulación de expresiones que contienen funciones trigonométricas se prefiere  utilizar la función `trigsimp`.

Si en lugar de reducir una expresión trigonométrica se requiere expandirla, también existe la función `expand_trig`, la cual maneja de mejor manera las manipulaciones trigonométricas:

%% code prov-43
sy.expand_trig( sy.sin(x+y) )

%% md prov-44
## 5. Sustituciones

%% md prov-45

## 5.1 Sustituciones simbólicas simples

En `SymPy`, podemos sustituir una variable simbólica por otra variable, expresión o valor numérico. Esta funcionalidad es especialmente útil cuando deseamos evaluar expresiones en puntos específicos o simplificar expresiones sustituyendo variables por otras relaciones conocidas. El método para esto es `.subs`.

%% code prov-46
expr = sy.cos(x)**2 + sy.sin(x)**2
expr

%% md prov-47
Ahora sustituiremos $x$ por $y^2$ usando el método `.susb` de una expresión como se muestra a continuación:

%% code prov-48
expr2 = expr.subs(x, y**2)
expr2

%% md prov-49
Hay que tener en cuenta que la expresión que está guardada en la variable, `expr` no cambia. Cuando se aplica el método `.subs ` devuelve la expresión modificada pero sin modificar la original.



%% code prov-50
expr

%% md prov-51
## 5.2  Sustitución simbólica de una Expresión Compleja

Podemos realizar sustituciones más complejas, como reemplazar $\sin(x)
$ con la función exponencial $e^x$. Esto puede ser útil en contextos donde queramos expresar funciones trigonométricas en términos de otras funciones.

%% code prov-52
expr.subs(sy.sin(x), sy.exp(x))

%% md prov-53
## 5.3 Sustitución Numérica
Para evaluar una expresión en un valor específico de una variable, usamos también .subs, seguido del valor deseado:

%% code prov-54
expr.subs(x,3)

%% md prov-55
Esta instrucción reemplaza $x$ por $3$ en la expresión `expr`. Sin embargo, el resultado podría no ser decimal a menos que incluyamos el método `.evalf()`.


%% md prov-56
## 5.4 Evaluación Numérica con `.evalf()`

El método `.evalf()` permite obtener un resultado decimal de una expresión después de realizar sustituciones numéricas. Por ejemplo, si deseamos obtener un resultado decimal con precisión de 7 dígitos, podemos hacer lo siguiente:

%% code prov-57
expresion =  sy.exp(x)
print('la expresión es: ')
display(expresion)
valor = expresion.subs(x,5).evalf(7)
print(f'Si reemplazamos x por 5 y la avaluamos con 7 dígitos obtenemos: {valor}')


%% md prov-58
Si queremos resultados exactos en formato de fracción en vez de decimales, podemos utilizar `sy.Rational` para especificar valores en forma de fracción:

%% code prov-59
expr = x**2 / 4
expr_frac = expr.subs(x, sy.Rational(3, 2))
expr_frac


%% md prov-60
Esta última expresión mantendrá la precisión fraccionaria en lugar de convertir los valores a decimales, lo cual es especialmente útil en contextos donde se requieren respuestas exactas.

%% md prov-61
## 6. Resolución de Ecuaciones

Una de las funciones más útiles de `SymPy` es `solve`, la cual permite resolver una amplia variedad de ecuaciones, desde ecuaciones polinomiales y sistemas lineales hasta inecuaciones y sistemas no lineales. La sintaxis de `solve` se adapta automáticamente a la ecuación o sistema dado, permitiendo resolver con una estructura muy simple.

Para comenzar, recordemos que `SymPy` trata las ecuaciones como expresiones algebraicas. Esto significa que para resolver una ecuación, el término que queremos igualar a cero debe ser pasado como argumento en la función `solve`. Veamos algunos ejemplos básicos.

### Ejemplo 1: Ecuación Lineal

Para resolver una ecuación simple como \( x - 3 = 0 \), pasamos la expresión `x - 3` a `solve`, asumiendo que está igualada a cero. `solve` nos devolverá el valor de \( x \) que satisface la ecuación.



%% code act-01
x = sy.symbols("x")

# Resolver ecuación lineal
solucion = sy.solve(x - 3)
print("Solución de la ecuación lineal:", solucion)

%% md prov-62
### Ejemplo 2: Ecuación Cuadrática

Si la ecuación es cuadrática, `solve` buscará soluciones tanto reales como complejas. Para resolver \( x^2 + 2x + 2 = 0 \):



%% code act-02
# Resolver ecuación cuadrática
solucion_cuadratica = sy.solve(x**2 + 2*x + 2)
print("Soluciones de la ecuación cuadrática:", solucion_cuadratica)


%% md prov-63
Aquí, el resultado incluye soluciones complejas, ya que esta ecuación no tiene raíces reales.


%% md prov-64
### Ejemplo 3: Resolver para una Variable Específica

Cuando trabajamos con ecuaciones que incluyen múltiples variables, debemos indicar la variable sobre la cual queremos resolver. Esto es útil para ecuaciones cuadráticas en su forma general, por ejemplo:

$$
a x^2 + b x + c = 0
$$


%% code act-03
a, b, c = sy.symbols("a b c")
expresion = a*x**2 + b*x + c

# Resolver ecuación general cuadrática para x
solucion_general = sy.solve(expresion, x)
print("Solución general de la ecuación cuadrática:")

solucion_general


%% md prov-65
### Ejemplo 4: Sistema de Ecuaciones

`SymPy` también permite resolver sistemas de ecuaciones simultáneas. Para resolver el siguiente sistema:

$$
\begin{cases}
x + y = 5 \\
x - y = 1 \\
\end{cases}
$$

Primero definimos las ecuaciones y luego las pasamos a `solve` en forma de lista.


%% code act-04
y = sy.symbols("y")
# Definir el sistema de ecuaciones
ecuacion1 = x + y - 5
ecuacion2 = x - y - 1

# Resolver el sistema
solucion_sistema = sy.solve((ecuacion1, ecuacion2), (x, y))
print("Solución del sistema de ecuaciones:", solucion_sistema)


%% md prov-66
En este caso, `solve` devolverá un diccionario con los valores de `x` e `y` que satisfacen ambas ecuaciones.


%% code act-05
# Resolver ecuación no lineal
solucion_no_lineal = sy.solve(x**3 - x + 1)
print("Soluciones de la ecuación no lineal:")
solucion_no_lineal

%% md prov-67
## 7. Derivadas e Integrales

SymPy ofrece potentes herramientas para el cálculo simbólico de derivadas e integrales, lo que permite realizar estos cálculos sin necesidad de valores específicos para las variables. A continuación, exploraremos cómo calcular derivadas e integrales de expresiones algebraicas en SymPy, con ejemplos básicos y avanzados.


%% md prov-68
#### 7.1 Derivadas

Para calcular la derivada de una expresión en `SymPy`, usamos la función `diff`. Esta función espera al menos dos argumentos: una expresión algebraica y una variable respecto a la cual se derivará. Veamos algunos ejemplos:





%% code prov-69
x = sy.symbols("x")
exp=sy.exp(x) * sy.cos(x)
print("La expresión es:")
display(exp)
# Derivada de una función exponencial multiplicada por una función trigonométrica
print("La derivada de la expresión es:")
exp_deriv=sy.diff(exp, x)
display(exp_deriv)

%% md prov-70
Para calcular derivadas de orden superior, podemos pasar un tercer argumento a `diff` indicando el orden de la derivada:


%% code prov-71
# Derivada segunda de la función 5x^2 + 3x - 10 con respecto a x
sy.diff(5 * x**2 + 3 * x - 10, x, 2)


%% md prov-72
Aquí calculamos la derivada segunda de $f(x) = 5x^2 + 3x - 10 $, que se indica con el último argumento `2`.




%% md prov-73
Además, `SymPy` permite calcular derivadas parciales de funciones de varias variables simplemente especificando la variable respecto a la cual queremos derivar. Ejemplo:


%% code prov-74
y, z = sy.symbols("y z")
f = sy.exp(x*y) + sy.sin(z)
# Derivada parcial con respecto a y
sy.diff(f, y)


%% md prov-75
Este código calcula la derivada parcial de $e^{xy} + \sin(z) $ con respecto a \( y \).


%% md prov-76
### 7.2 Integrales

La función `integrate` de `SymPy` permite calcular integrales simbólicas. Para integrales indefinidas, simplemente pasamos la función a integrar y la variable de integración:



%% code prov-77
# Integral indefinida de x^2 + 3x - 7 con respecto a x
sy.integrate(x**2 + 3 * x - 7, x)


%% md prov-78
Esa instrucción calcula la siguiente integral:

$$ \int \left( x^2 + 3x - 7 \, \right) \,\, dx = \frac{x^3}{3} + \frac{3x^2}{2} - 7x + C $$

La salida será la primitiva de \( x^2 + 3x - 7 \) respecto a \( x \), sin la constante de integración.


Si deseamos calcular una integral definida, podemos pasar una tupla como segundo argumento de la forma `(variable, a, b)`, donde `a` y `b` son los límites de integración:


Por ejemplo, para evaluar:

$$ \int_0^{\pi} \sin x \, dx $$


%% code prov-79
# Integral definida de z^2 desde -5 hasta 5
z = sy.symbols("z")
sy.integrate(z**2, (z, -5, 5))


%% md prov-80
SymPy también permite integrar funciones más complejas, como polinomios o funciones exponenciales, en cualquier intervalo que definamos.


%% md prov-81
## 8. Funciones útiles


%% md prov-82
### 8.1 `sy.plot()`

Podemos usar la función sy.plot() para graficar funciones simbólicas. Su uso es el siguiente, la función `sym.plot(f, (x,a, b))` grafica la expresión `f`, tomando la variable `x` desde el valor `a` hasta el valor `b`.

%% code prov-83
x = sy.symbols('x')
f = x**2 - 2*x + 1

sy.plot(f, (x,-200, 200))

%% md prov-84
### 8.1 `sy.Piecewise`

Otra función útil es `sy.Piecewise()`. Esta nos permite definir funciones por tramos.

Toma como argumento una secuencia de tuplas, donde cada tupla tiene dos elementos: una expresión  de función y una condición que indica el intervalo de la variable independiente donde aplica esa función.

 `sy.Piecewise((expresión_1, condición_1), (expresión_2, condición_2)...(expresión_n, condición_n))`

 Esto nos permite conformar funciones como la siguiente

$$
f(x) =  \begin{cases}
      x^2 & \text{si } x < 0 \\
      0.1  x^3 & \text{si } x \geq 0
   \end{cases}
$$

 En el siguiente ejemplo, la función f vale $x^2$ cuando $x$ es menor que cero y $(0.1 x^3)$ cuando $x$ es mayor o igual a cero.

%% code prov-85
# Definir la función piecewise
f = sy.Piecewise((x**2, x < 0), (0.1*x**3, x >= 0))

# Podemos usar la función sym.plot() para graficar funciones simbólicas
sy.plot(f, (x,-200, 200))

%% md prov-86
----
Con esto llegamos al final de este tutorial! Recuerda que los temas que desarrollamos en los tutoriales de la cátedra son tratados de manera básica y contienen solo lo necesario para poder presentar de forma didáctica los contenidos de la asignatura. Entender Python en profundidad requiere un curso completo dedicado a ello.

En [este link](https://github.com/vinta/awesome-python)  encontrarás una extensa cantidad de librerías de python para trabajar prácticamente sobre cualquier temática que necesites.

En [este link](https://docs.python.org/es/3.9/) encontrarás la documentación completa de Python

En [este link](https://docs.sympy.org/latest/index.html) encontrarás la documentación completa de SymPy.


Cualquier comentario no dudes en consultar con los profesores de la cátedra.

