# Answer found in Q5 in Question Bank 1 (Tan et al, 2nd ed)

# import student_code_with_answers.utils as u
import utils as u
import math as m

# Example of how to specify a binary with the structure:
# See the file INSTRUCTIONS.md
# ----------------------------------------------------------------------


def question1():
    """
    Note 1: Each attribute can appear as a node in the tree AT MOST once.
    Note 2: For level two, fill the keys for all cases left and right. If and attribute
    is not considered for level 2, set the values to -1. For example, if "flu" were the
    choice for level 1 (it is not), then set level2_left['flu'] = level2_right['flu'] = -1.,
    and the same for keys 'flu_info_gain'.
    """
    answer = False
    answer = {}
    level1 = {}
    level2_left = {}
    level2_right = {}

    level1["smoking"] = 1.0
    level1["smoking_info_gain"] =0.2780719051126377
#   values(tobacco smoking)= yes,no
#   total entropy= [5+(yes),5-(no)] = -5/10(log2(5/10))-5/10(log2(5/10))=1
#   entropy of yes= [4+(yes),1-(no)]= -1/5(log2(1/5))-4/5(log2(4/5)) =0.721928....
#   entropy of yes= [1+(yes),4-(no)]= -4/5(log2(4/5))-1/5(log2(1/5)) =0.721928....
#   gain of tobacco smoking = 1-(5/10)(0.721928....)-(5/10)(0.721928....) = 0.2780719051126377
    level1["cough"] = -1.0
    level1["cough_info_gain"] =0.034851554559677034
#   values(caugh)= yes,no
#   total entropy= [5+(yes),5-(no)] = -5/10(log2(5/10))-5/10(log2(5/10))=1
#   entropy of yes= [4+(yes),3-(no)]= -4/5(log2(4/5))-3/5(log2(3/5)) =0.98522....
#   entropy of yes= [1+(yes),2-(no)]= -1/5(log2(1/5))-2/5(log2(2/5)) =0.91829....
#   gain of caugh = 1-(7/10)(0.98522....)-(3/10)(0.91829....) = 0.2780719051126377
    level1["radon"] = -1.0
    level1["radon_info_gain"] = 0.23645279766002802

    level1["weight_loss"] = -1.0
    level1["weight_loss_info_gain"] = 0.02904940554533142

    level2_left["smoking"] = -1.0
    level2_left["smoking_info_gain"] = 0.0
    level2_right["smoking"] = -1.0
    level2_right["smoking_info_gain"] = 0.0

    level2_left["radon"] = -1.0
    level2_left["radon_info_gain"] = 0.07290559532005603

    level2_left["cough"] = 1.0
    level2_left["cough_info_gain"] = 0.7219280948873623

    level2_left["weight_loss"] = -1.0
    level2_left["weight_loss_info_gain"] = 0.17095059445466865

    level2_right["radon"] = 1.0
    level2_right["radon_info_gain"] =0.7219280948873623

    level2_right["cough"] = -1.0
    level2_right["cough_info_gain"] = 0.0

    level2_right["weight_loss"] = -1.0
    level2_right["weight_loss_info_gain"] = 0.17095059445466865

    answer["level1"] = level1
    answer["level2_left"] = level2_left
    answer["level2_right"] = level2_right

    tree=u.BinaryTree("smoking")
    A=tree.insert_left("cough")
    B=tree.insert_right("radon")
    A.insert_left("Yes")
    A.insert_right("No")
    B.insert_left("Yes")
    B.insert_right("No")
    answer["tree"] = tree  
    answer["training_error"] = 0.0   

    return answer

# ----------------------------------------------------------------------


def question2():
    answer = {}

    # Answers are floats
    answer["(a) entropy_entire_data"] = 1.4253642047367425
    #area of a is
    area_a = ((0.3 * 0.3) + (0.8 * 0.4)) 
    area_b = ((0.7 * 0.6) + (0.2 * 0.2)) 
    area_c = ((0.2 * 0.2) + (0.3 * 0.3)) 
    area_total = area_a + area_b + area_c
    entropy_area = -(((area_a) * u.log2(area_a)) + ((area_b) * u.log2(area_b)) + ((area_c) * u.log2(area_c)))
    print("2a - The entropy for the overall data is: " + str(entropy_area))


    # Infogain
    answer["(b) x < 0.2"] = 0.17739286055515824
    #2-b for x < = 0.2
    area_x_2_l_a = 0
    area_x_2_l_b = ((0.2 * 0.6) + (0.2 * 0.2))
    area_x_2_l_c = (0.2 * 0.2)
    area_x_2_g_a = ((0.8 * 0.4) + (0.3 * 0.3))
    area_x_2_g_b = (0.5 * 0.6)
    area_x_2_g_c = (0.3 * 0.3)
    area_x_2_l_tot = area_x_2_l_a + area_x_2_l_b + area_x_2_l_c
    area_x_2_g_tot = area_x_2_g_a + area_x_2_g_b + area_x_2_g_c
    area_x_2_tot = area_x_2_l_tot + area_x_2_g_tot
    entropy_x_2_l = -(((area_x_2_l_b/area_x_2_l_tot) * (u.log2(area_x_2_l_b/area_x_2_l_tot))) + ((area_x_2_l_c/area_x_2_l_tot) * (u.log2(area_x_2_l_c/area_x_2_l_tot))))
    entropy_x_2_g = -(((area_x_2_g_a/area_x_2_g_tot) * (u.log2(area_x_2_g_a/area_x_2_g_tot))) + ((area_x_2_g_b/area_x_2_g_tot) * (u.log2(area_x_2_g_b/area_x_2_g_tot))) + ((area_x_2_g_c/area_x_2_g_tot) * (u.log2(area_x_2_g_c/area_x_2_g_tot))))
    entropy_x_2 = ((area_x_2_l_tot/area_x_2_tot) * entropy_x_2_l) + ((area_x_2_g_tot/area_x_2_tot) * entropy_x_2_g) 
    entropy_x_2_gain = entropy_area - entropy_x_2
    print("2b - The information gain for split x<= 0.2 is: " + str(entropy_x_2_gain))

    answer["(b) x < 0.7"] = 0.3557029418697566
    #2-b for x < = 0.7
    area_x_7_l_a = (0.5 * 0.4)
    area_x_7_l_b = ((0.7 * 0.6) + (0.2 * 0.2))
    area_x_7_l_c = (0.2 * 0.2)
    area_x_7_g_a = ((0.3 * 0.4) + (0.3 * 0.3))
    area_x_7_g_b = 0
    area_x_7_g_c = (0.3 * 0.3)
    area_x_7_l_tot = area_x_7_l_a + area_x_7_l_b + area_x_7_l_c
    area_x_7_g_tot = area_x_7_g_a + area_x_7_g_b + area_x_7_g_c
    area_x_7_tot = area_x_7_l_tot + area_x_7_g_tot
    entropy_x_7_l = -(((area_x_7_l_a/area_x_7_l_tot) * (u.log2(area_x_7_l_a/area_x_7_l_tot))) + ((area_x_7_l_b/area_x_7_l_tot) * (u.log2(area_x_7_l_b/area_x_7_l_tot))) + ((area_x_7_l_c/area_x_7_l_tot) * (u.log2(area_x_7_l_c/area_x_7_l_tot))))
    entropy_x_7_g = -(((area_x_7_g_a/area_x_7_g_tot) * (u.log2(area_x_7_g_a/area_x_7_g_tot))) + ((area_x_7_g_c/area_x_7_g_tot) * (u.log2(area_x_7_g_c/area_x_7_g_tot))))
    entropy_x_7 = ((area_x_7_l_tot/area_x_7_tot) * entropy_x_7_l) + ((area_x_7_g_tot/area_x_7_tot) * entropy_x_7_g) 
    entropy_x_7_gain = entropy_area - entropy_x_7
    print("2b - The information gain for split x<= 0.7 is: " + str(entropy_x_7_gain))

    answer["(b) y < 0.6"] = 0.34781842724338197
    #2-b for y < = 0.6
    area_y_6_l_a = (0.3 * 0.3)
    area_y_6_l_b = (0.7 * 0.6) 
    area_y_6_l_c = (0.3 * 0.3)
    area_y_6_g_a = (0.8 * 0.4)
    area_y_6_g_b = (0.2 * 0.2)
    area_y_6_g_c = (0.2 * 0.2)
    area_y_6_l_tot = area_y_6_l_a + area_y_6_l_b + area_y_6_l_c
    area_y_6_g_tot = area_y_6_g_a + area_y_6_g_b + area_y_6_g_c
    area_y_6_tot = area_y_6_l_tot + area_y_6_g_tot
    entropy_y_6_l = -(((area_y_6_l_a/area_y_6_l_tot) * (u.log2(area_y_6_l_a/area_y_6_l_tot))) + ((area_y_6_l_b/area_y_6_l_tot) * (u.log2(area_y_6_l_b/area_y_6_l_tot))) + ((area_y_6_l_c/area_y_6_l_tot) * (u.log2(area_y_6_l_c/area_y_6_l_tot))))
    entropy_y_6_g = -(((area_y_6_g_a/area_y_6_g_tot) * (u.log2(area_y_6_g_a/area_y_6_g_tot))) + ((area_y_6_g_b/area_y_6_g_tot) * (u.log2(area_y_6_g_b/area_y_6_g_tot))) + ((area_y_6_g_c/area_y_6_g_tot) * (u.log2(area_y_6_g_c/area_y_6_g_tot))))
    entropy_y_6 = ((area_y_6_l_tot/area_y_6_tot) * entropy_y_6_l) + ((area_y_6_g_tot/area_y_6_tot) * entropy_y_6_g) 
    entropy_y_6_gain = entropy_area - entropy_y_6
    print("2b - The information gain for split y<= 0.6 is: " + str(entropy_y_6_gain))

    # choose one of 'x=0.2', 'x=0.7', or 'y=0.6'
    answer["(c) attribute"] = "x=0.7"  

    #2-b entropy at left after split x = 0.7


    #2-b for x < = 0.2 at level 2 left
    area_x1_2_l_a = 0
    area_x1_2_l_b = (0.2 * 0.2) + (0.2 * 0.6) 
    area_x1_2_l_c = (0.2 * 0.2)
    area_x1_2_l_tot = area_x1_2_l_a + area_x1_2_l_b + area_x1_2_l_c
    area_x1_2_g_a = (0.5 * 0.4)
    area_x1_2_g_b = (0.5 * 0.6)
    area_x1_2_g_c = 0
    area_x1_2_g_tot = area_x1_2_g_a + area_x1_2_g_b + area_x1_2_g_c
    area_x1_2_tot = area_x1_2_l_tot + area_x1_2_g_tot
    entropy_x1_2_l = -(((area_x1_2_l_a/area_x1_2_l_tot) * 0) + ((area_x1_2_l_b/area_x1_2_l_tot) * (u.log2(area_x1_2_l_b/area_x1_2_l_tot))) + ((area_x1_2_l_c/area_x1_2_l_tot) * (u.log2(area_x1_2_l_c/area_x1_2_l_tot))))
    entropy_x1_2_g = -(((area_x1_2_g_a/area_x1_2_g_tot) * (u.log2(area_x1_2_g_a/area_x1_2_g_tot))) + ((area_x1_2_g_b/area_x1_2_g_tot) * (u.log2(area_x1_2_g_b/area_x1_2_g_tot))) + ((area_x1_2_g_c/area_x1_2_g_tot) * 0))
    entropy_x1_2 = ((area_x1_2_l_tot/area_x1_2_tot) * entropy_x1_2_l) + ((area_x1_2_g_tot/area_x1_2_tot) * entropy_x1_2_g) 
    entropy_x1_2_gain = (entropy_x_7 - entropy_x1_2)
    print("2b - The information gain for split x<= 0.2 at level 2 left is: " + str(entropy_x1_2_gain))

    #2-b for y < = 0.6 at level 2 left
    area_y1_6_l_a = 0
    area_y1_6_l_b = (0.7 * 0.6) 
    area_y1_6_l_c = 0
    area_y1_6_l_tot = area_y1_6_l_a + area_y1_6_l_b + area_y1_6_l_c
    area_y1_6_g_a = (0.5 * 0.4)
    area_y1_6_g_b = 0.04
    area_y1_6_g_c = 0.04
    area_y1_6_g_tot = area_y1_6_g_a + area_y1_6_g_b + area_y1_6_g_c
    area_y1_6_tot = area_y1_6_l_tot + area_y1_6_g_tot
    entropy_y1_6_l = -(((area_y1_6_l_a/area_y1_6_l_tot) * 0) + ((area_y1_6_l_b/area_y1_6_l_tot) * (u.log2(area_y1_6_l_b/area_y1_6_l_tot))) + ((area_y1_6_l_c/area_y1_6_l_tot) * 0))
    entropy_y1_6_g = -(((area_y1_6_g_a/area_y1_6_g_tot) * (u.log2(area_y1_6_g_a/area_y1_6_g_tot))) + ((area_y1_6_g_b/area_y1_6_g_tot) * (u.log2(area_y1_6_g_b/area_y1_6_g_tot))) + ((area_y1_6_g_c/area_y1_6_g_tot) * (u.log2(area_y1_6_g_c/area_y1_6_g_tot))))
    entropy_y1_6 = ((area_y1_6_l_tot/area_y1_6_tot) * entropy_y1_6_l) + ((area_y1_6_g_tot/area_y1_6_tot) * entropy_y1_6_g) 
    entropy_y1_6_gain = (entropy_x_7 - entropy_y1_6)
    print("2b - The information gain for split y<= 0.6 at level 2 left is: " + str(entropy_y1_6_gain))

    #2-b for y < = 0.3 at level 2 left
    area_y1_3_l_a = 0
    area_y1_3_l_b = (0.3 * 0.7) 
    area_y1_3_l_c = 0
    area_y1_3_l_tot = area_y1_3_l_a + area_y1_3_l_b + area_y1_3_l_c
    area_y1_3_g_a = (0.5 * 0.4)
    area_y1_3_g_b = (0.04 + (0.7 * 0.3))
    area_y1_3_g_c = 0.04
    area_y1_3_g_tot = area_y1_3_g_a + area_y1_3_g_b + area_y1_3_g_c
    area_y1_3_tot = area_y1_3_l_tot + area_y1_3_g_tot
    entropy_y1_3_l = -(((area_y1_3_l_a/area_y1_3_l_tot) * 0) + ((area_y1_3_l_b/area_y1_3_l_tot) * (u.log2(area_y1_3_l_b/area_y1_3_l_tot))) + ((area_y1_3_l_c/area_y1_3_l_tot) * 0))
    entropy_y1_3_g = -(((area_y1_3_g_a/area_y1_3_g_tot) * (u.log2(area_y1_3_g_a/area_y1_3_g_tot))) + ((area_y1_3_g_b/area_y1_3_g_tot) * (u.log2(area_y1_3_g_b/area_y1_3_g_tot))) + ((area_y1_3_g_c/area_y1_3_g_tot) * (u.log2(area_y1_3_g_c/area_y1_3_g_tot))))
    entropy_y1_3 = ((area_y1_3_l_tot/area_y1_6_tot) * entropy_y1_3_l) + ((area_y1_3_g_tot/area_y1_3_tot) * entropy_y1_3_g) 
    entropy_y1_3_gain = (entropy_x_7 - entropy_y1_3)
    print("2b - The information gain for split y<= 0.3 at level 2 left is: " + str(entropy_y1_3_gain))   

    #2-b for y < = 0.8 at level 2 left
    area_y1_8_l_a = (0.5 * 0.2)
    area_y1_8_l_b = (0.6 * 0.7) 
    area_y1_8_l_c = (0.2 * 0.2)
    area_y1_8_l_tot = area_y1_8_l_a + area_y1_8_l_b + area_y1_8_l_c
    area_y1_8_g_a = (0.5 * 0.2)
    area_y1_8_g_b = (0.2 * 0.2)
    area_y1_8_g_c = 0
    area_y1_8_g_tot = area_y1_8_g_a + area_y1_8_g_b + area_y1_8_g_c
    area_y1_8_tot = area_y1_8_l_tot + area_y1_8_g_tot
    entropy_y1_8_l = -(((area_y1_8_l_a/area_y1_8_l_tot) * (u.log2(area_y1_8_l_a/area_y1_8_l_tot))) + ((area_y1_8_l_b/area_y1_8_l_tot) * (u.log2(area_y1_8_l_b/area_y1_8_l_tot))) + ((area_y1_8_l_c/area_y1_8_l_tot) * (u.log2(area_y1_8_l_c/area_y1_8_l_tot))))
    entropy_y1_8_g = -(((area_y1_8_g_a/area_y1_8_g_tot) * (u.log2(area_y1_8_g_a/area_y1_8_g_tot))) + ((area_y1_8_g_b/area_y1_8_g_tot) * (u.log2(area_y1_8_g_b/area_y1_8_g_tot))) + ((area_y1_8_g_c/area_y1_8_g_tot) * 0))
    entropy_y1_8 = ((area_y1_8_l_tot/area_y1_8_tot) * entropy_y1_8_l) + ((area_y1_8_g_tot/area_y1_8_tot) * entropy_y1_8_g) 
    entropy_y1_8_gain = (entropy_x_7 - entropy_y1_8)
    print("2b - The information gain for split y<= 0.8 at level 2 left is: " + str(entropy_y1_8_gain)) 

    #2-b for x < =  0.2, y > 0.6 right level 3
    area_y3_3_l_a = 0
    area_y3_3_l_b = 0.04 
    area_y3_3_l_c = 0.04
    area_y3_3_l_tot = area_y3_3_l_a + area_y3_3_l_b + area_y3_3_l_c
    area_y3_3_g_a = (0.5 * 0.4)
    area_y3_3_g_b = 0
    area_y3_3_g_c = 0
    area_y3_3_g_tot = area_y3_3_g_a + area_y3_3_g_b + area_y3_3_g_c
    area_y3_3_tot = area_y3_3_l_tot + area_y3_3_g_tot
    entropy_y3_3_l = -(((area_y3_3_l_a/area_y3_3_l_tot) * 0) + ((area_y3_3_l_b/area_y3_3_l_tot) * (u.log2(area_y3_3_l_b/area_y3_3_l_tot))) + ((area_y3_3_l_c/area_y3_3_l_tot) * (u.log2(area_y3_3_l_c/area_y3_3_l_tot))))
    entropy_y3_3_g = -(((area_y3_3_g_a/area_y3_3_g_tot) * (u.log2(area_y3_3_g_a/area_y3_3_g_tot))) + ((area_y3_3_g_b/area_y3_3_g_tot) * 0) + ((area_y3_3_g_c/area_y3_3_g_tot) * 0))
    entropy_y3_3 = ((area_y3_3_l_tot/area_y3_3_tot) * entropy_y3_3_l) + ((area_y3_3_g_tot/area_y3_3_tot) * entropy_y3_3_g) 
    entropy_y3_3_gain = (entropy_y1_6 - entropy_y3_3)
    print("2b - The information gain for split x<= 0.2 at level 3 right is: " + str(entropy_y3_3_gain))

    #2-b for y < =  0.8, y > 0.6 right level 3
    area_y4_3_l_a = (0.5 * 0.2)
    area_y4_3_l_b = 0
    area_y4_3_l_c = 0.04
    area_y4_3_l_tot = area_y4_3_l_a + area_y4_3_l_b + area_y4_3_l_c
    area_y4_3_g_a = (0.5 * 0.2)
    area_y4_3_g_b = 0.04
    area_y4_3_g_c = 0
    area_y4_3_g_tot = area_y4_3_g_a + area_y4_3_g_b + area_y4_3_g_c
    area_y4_3_tot = area_y4_3_l_tot + area_y4_3_g_tot
    entropy_y4_3_l = -(((area_y4_3_l_a/area_y4_3_l_tot) * (u.log2(area_y4_3_l_a/area_y4_3_l_tot))) + ((area_y4_3_l_b/area_y4_3_l_tot) * 0) + ((area_y4_3_l_c/area_y4_3_l_tot) * (u.log2(area_y4_3_l_c/area_y4_3_l_tot))))
    entropy_y4_3_g = -(((area_y4_3_g_a/area_y4_3_g_tot) * (u.log2(area_y4_3_g_a/area_y4_3_g_tot))) + ((area_y4_3_g_b/area_y4_3_g_tot) * (u.log2(area_y4_3_g_a/area_y4_3_g_tot))) + ((area_y4_3_g_c/area_y4_3_g_tot) * 0))
    entropy_y4_3 = ((area_y4_3_l_tot/area_y1_6_tot) * entropy_y4_3_l) + ((area_y4_3_g_tot/area_y4_3_tot) * entropy_y4_3_g) 
    entropy_y4_3_gain = (entropy_y1_6 - entropy_y4_3)
    print("2b - The information gain for split y<= 0.8 at level 3 right is: " + str(entropy_y4_3_gain))

    # We choose x < = 0.2 for level 3 right 

    #2-b for y<0.6 at level 2 right
    area_y2_3_l_a = 0.09
    area_y2_3_l_b = 0 
    area_y2_3_l_c = 0.09
    area_y2_3_l_tot = area_y2_3_l_a + area_y2_3_l_b + area_y2_3_l_c
    area_y2_3_g_a = (0.4 * 0.3)
    area_y2_3_g_b = 0
    area_y2_3_g_c = 0
    area_y2_3_g_tot = area_y2_3_g_a + area_y2_3_g_b + area_y2_3_g_c
    area_y2_3_tot = area_y2_3_l_tot + area_y2_3_g_tot
    entropy_y2_3_l = -(((area_y2_3_l_a/area_y2_3_l_tot) * (u.log2(area_y2_3_l_a/area_y2_3_l_tot))) + ((area_y2_3_l_b/area_y2_3_l_tot) * 0) + ((area_y2_3_l_c/area_y2_3_l_tot) * (u.log2(area_y2_3_l_c/area_y2_3_l_tot))))
    entropy_y2_3_g = -(((area_y2_3_g_a/area_y2_3_g_tot) * (u.log2(area_y2_3_g_a/area_y2_3_g_tot))) + ((area_y2_3_g_b/area_y2_3_g_tot) * 0) + ((area_y2_3_g_c/area_y2_3_g_tot) * 0))
    entropy_y2_3 = ((area_y2_3_l_tot/area_y2_3_tot) * entropy_y2_3_l) + ((area_y2_3_g_tot/area_y2_3_tot) * entropy_y2_3_g) 
    entropy_y2_3_gain = (entropy_x_7 - entropy_y2_3)
    print("2b - The information gain for split y<= 0.6 at level 2 right is: " + str(entropy_y2_3_gain)) 

    #2-b for y<0.3 at level 2 right
    area_y5_3_l_a = 0.09
    area_y5_3_l_b = 0 
    area_y5_3_l_c = 0
    area_y5_3_l_tot = area_y5_3_l_a + area_y5_3_l_b + area_y5_3_l_c
    area_y5_3_g_a = (0.4 * 0.3)
    area_y5_3_g_b = 0
    area_y5_3_g_c = 0.09
    area_y5_3_g_tot = area_y5_3_g_a + area_y5_3_g_b + area_y5_3_g_c
    area_y5_3_tot = area_y5_3_l_tot + area_y5_3_g_tot
    entropy_y5_3_l = -(((area_y5_3_l_a/area_y5_3_l_tot) * (u.log2(area_y5_3_l_a/area_y5_3_l_tot))) + ((area_y5_3_l_b/area_y5_3_l_tot) * 0) + ((area_y5_3_l_c/area_y5_3_l_tot) * 0))
    entropy_y5_3_g = -(((area_y5_3_g_a/area_y5_3_g_tot) * (u.log2(area_y5_3_g_a/area_y5_3_g_tot))) + ((area_y5_3_g_b/area_y5_3_g_tot) * 0) + ((area_y5_3_g_c/area_y5_3_g_tot) * (u.log2(area_y5_3_g_c/area_y5_3_g_tot))))
    entropy_y5_3 = ((area_y5_3_l_tot/area_y5_3_tot) * entropy_y5_3_l) + ((area_y5_3_g_tot/area_y5_3_tot) * entropy_y5_3_g) 
    entropy_y5_3_gain = (entropy_x_7 - entropy_y5_3)
    print("2b - The information gain for split y<= 0.3 at level 2 right is: " + str(entropy_y5_3_gain)) 

    #2-b for y<0.8 at level 2 right
    area_y6_3_l_a = (0.09 + (0.2 * 0.3))
    area_y6_3_l_b = 0 
    area_y6_3_l_c = 0.09
    area_y6_3_l_tot = area_y6_3_l_a + area_y6_3_l_b + area_y6_3_l_c
    area_y6_3_g_a = 0.06
    area_y6_3_g_b = 0
    area_y6_3_g_c = 0
    area_y6_3_g_tot = area_y6_3_g_a + area_y6_3_g_b + area_y6_3_g_c
    area_y6_3_tot = area_y6_3_l_tot + area_y6_3_g_tot
    entropy_y6_3_l = -(((area_y6_3_l_a/area_y6_3_l_tot) * (u.log2(area_y6_3_l_a/area_y6_3_l_tot))) + ((area_y6_3_l_b/area_y6_3_l_tot) * 0) + ((area_y6_3_l_c/area_y6_3_l_tot) * (u.log2(area_y6_3_l_c/area_y6_3_l_tot))))
    entropy_y6_3_g = -(((area_y6_3_g_a/area_y6_3_g_tot) * (u.log2(area_y6_3_g_a/area_y6_3_g_tot))) + ((area_y6_3_g_b/area_y6_3_g_tot) * 0) + ((area_y6_3_g_c/area_y6_3_g_tot) * 0))
    entropy_y6_3 = ((area_y6_3_l_tot/area_y6_3_tot) * entropy_y6_3_l) + ((area_y6_3_g_tot/area_y6_3_tot) * entropy_y6_3_g) 
    entropy_y6_3_gain = (entropy_x_7 - entropy_y6_3)
    print("2b - The information gain for split y<= 0.8 at level 2 right is: " + str(entropy_y6_3_gain)) 

    # we select y<= 0.6 for level 2 right and the left child to this is y <= 0.3

    # Use the Binary Tree structure to construct the tree
    # Answer is an instance of BinaryTree
    tree = u.BinaryTree("x <= 0.7")
    A = tree.insert_left("y <= 0.6")
    B = tree.insert_right("y <= 0.6")
    C = A.insert_right ("x <= 0.2")
    D = C.insert_left("y <= 0.8")
    E = B.insert_left("y <= 0.3")
    A.insert_left("B")
    C.insert_right("A")
    D.insert_left("C")
    D.insert_right("B")
    B.insert_right("A")
    E.insert_left("A")
    E.insert_right("C")
    
    answer["(d) full decision tree"] = tree
    return answer


# ----------------------------------------------------------------------

def gini(l):
    gini=0
    for i in l:
        gini+=i**2
    return 1-gini
def question3():
    answer = {}

    # float
    answer["(a) Gini, overall"] = 0.5
    
    p_co=10/20
    p_c1=10/20
    print(f'Gini index {gini([p_co,p_c1])}')
    # float
    answer["(b) Gini, ID"] = 0.0
    gini([1])
    # so  the gini impurity for all the players = 0 ,as it each cust ID will be unique
    id_wise=[(1/20)*0]*20
    id_wise   
   
    answer["(c) Gini, Gender"] = 0.48
    #weighted gini Index
    gm_co=6/10
    gm_c1=4/10
    gf_co=4/10
    gf_c1=6/10
    gini_gm=gini([gm_co,gm_c1])
    gini_gf=gini([gf_co,gf_c1])
    weighted_gini=gini_gm #As gini for both male and female is same avg 

    answer["(d) Gini, Car type"] = 0.16250000000000003
    cf_co=1/4
    cf_c1=3/4
    cs_co=8/8
    cs_c1=0
    cl_co=1/8
    cl_c1=7/8
    gini_cf=gini([cf_co,cf_c1])
    gini_cs=gini([cs_co,cs_c1])
    gini_cl=gini([cl_co,cl_c1])
    weighted_gini_car=(4/20)*gini_cf + gini_cs*(8/20) + gini_cl*(8/20)
    weighted_gini_car
    answer["(e) Gini, Shirt type"] = 0.49142857142857144
    ss_co=3/5
    ss_c1=2/5
    sm_co=3/7
    sm_c1=4/7
    sl_co=2/4
    sl_c1=2/4
    sxl_co=2/4
    sxl_c1=2/4
    gini_ss=gini([ss_co,ss_c1])
    gini_sm=gini([sm_co,sm_c1])
    gini_sl=gini([sl_co,sl_c1])
    gini_sxl=gini([sxl_co,sxl_c1])
    weighted_gini_shirt=(5/20)*gini_ss + gini_sm*(7/20) + gini_sl*(4/20) + gini_sxl*(4/20)
    print(weighted_gini_shirt)
    
    answer["(f) attr for splitting"] = "Car type"

    # Explanatory text string
    answer["(f) explain choice"] = "Based on the gini impurity metrics mentioned above, it appears that ID is the most appropriate for the initial split (root). However, generally speaking, for unseen/test sets, employing ID as the root does not yield valid/consistent results. Therefore, we must select the next least impurity. This was the first selection made using the car type."

    return answer


# ----------------------------------------------------------------------
# Answers in th form [str1, str2, str3]
# If both 'binary' and 'discrete' apply, choose 'binary'.
# str1 in ['binary', 'discrete', 'continuous']
# str2 in ['qualitative', 'quantitative']
# str3 in ['interval', 'nominal', 'ratio', 'ordinal']


def question4():
    answer = {}

    # [string, string, string]
    # Each string is one of ['binary', 'discrete', 'continuous', 'qualitative', 'nominal', 'ordinal',
    #  'quantitative', 'interval', 'ratio'
    # If you have a choice between 'binary' and 'discrete', choose 'binary'

    answer["a"] = ["binary, quantitative, nominal"]

    # Explain if there is more than one interpretation. Repeat for the other questions. At least five words that form a sentence.
    answer["a: explain"] = "Binary is used because time in AM or PM may be either discrete or binary (AM or PM can be represented by 0 or 1) and binary characteristics are regarded as notional."


    answer["b"] = ["continuous, quantitative, ratio"]
    answer["b: explain"] = "If the light meters have a real zero point, then it is a ratio; if not, it is an interval."


    answer["c"] = ["discrete, qualitative, ordinal"]
    answer["c: explain"] = "People may judge anything by saying that the light is brilliant, not so bright, etc., but addition and subtraction are not possible."


    answer["d"] = ["continuous, quantitative, ratio"]
    answer["d: explain"] = "In addition to having a genuine zero and being continuous, angles can also be 29.5 degrees, or a ratio."

    answer["e"] = ["discrete, qualitative, ordinal"]
    answer["e: explain"] = "There are just three medals available, thus ordering is necessary."

    answer["f"] = ["continuous, quantitative, ratio"]
    answer["f: explain"] = "Since sea level may be used as a genuine zero, it is a ratio."

    answer["g"] = ["discrete, quantitative, ratio"]
    answer["g: explain"] = "A hospital's patient population can be counted and expressed as a ratio."

    answer["h"] = ["discrete, qualitative, nominal"]
    answer["h: explain"] = "ISBN digits are distinct, have no numerical significance, and have no relationship to one another."


    answer["i"] = ["discrete, qualitative, ordinal"]
    answer["i: explain"] = "Although the rankings for light may be ranked, they are qualitative as they don't quantify the amount of light that passes through."


    answer["j"] = ["discrete, qualitative, ordinal"]
    answer["j: explain"] = "The ranks in the military are limited and can be arranged in relation to one another."


    answer["k"] = ["continuous, quantitative, ratio"]
    answer["k: explain"] = "Since the genuine zero may be the campus center, it is a ratio."


    answer["l"] = ["continuous, quantitative, ratio"]
    answer["l: explain"] = "Density is ratio because we can say a substance is 2 times as dense as another substance because it has zero point."

    answer["m"] = ["discrete, qualitative, nominal"]
    answer["m: explain"] = "Coat check numbers A number is just employed as a means of identification; it has no meaning of its own."


    return answer




# ----------------------------------------------------------------------


def question5():
    explain = {}

    # Read appropriate section of book chapter 3

    # string: one of 'Model 1' or 'Model 2'
    explain["a"] = "Model 2"
    explain["a explain"] = "Its because if a model perform 98'%' accuracy on trainset and 72'%' on test set, it indicates there is a lot of variance, indicates model might have overfitted on trainset"

    # string: one of 'Model 1' or 'Model 2'
    explain["b"] = "Model 2"
    explain["b explain"] = "Performance is almost the same 81 and 85 not much of a difference, but Occams Razor states that if model have identical performance, choose the one that has low complexity (here pruned model [model 2]) as it(pruning) ensures model from getting overfit"

    explain["c similarity"] = "Complexity Term"
    explain["c similarity explain"] = "If the model is complex (either depth or number of leaves), the complexity term in both the calculations(MDL and pessimistic) will penalize the error in the same direction. In case of Pessimistic if K is more, the penalty will be higher. Also in case of MDL when the children are high, the complexity increases."

    explain["c difference"] = "Representation of Weights and Errors"
    explain["c difference explain"] = "In MDL values are represent using bits, where as its not the same in case of Pessimistic Error"

    return explain


    return explain

# ----------------------------------------------------------------------
def question6():
    answer = {}
    # x <= ? is the left branch
    # y <= ? is the left branch

    # value of the form "z <= float" where "z" is "x" or "y"
    #  and "float" is a floating point number (notice: <=)
    # The value could also be "A" or "B" if it is a leaf
    answer["a, level 1"] = "x<=0.5"
    answer["a, level 2, right"] ="A"
    answer["a, level 2, left"] = "y<=0.4"
    answer["a, level 3, left"] = "A"
    answer["a, level 3, right"] = "x<=0.2"

    # When we move to right node of y =0.4
    # We pruned the tree (2 level) as class B, because only 6%(0.2*0.3) of A's will go through that decision, And rest all the A's have their own 
    err=0.2*0.3
    answer["b, expected error"] = err

    # Use u.BinaryTree to define the tree. Create your tree.
    # Replace "root node" by the proper node of the form "z <= float"
    tree = u.BinaryTree("x<=0.5")
    A=tree.insert_left("y<=0.4")
    C=A.insert_left('A')
    A.insert_right('x<=0.2')

    B=tree.insert_right("A")
    answer["c, tree"] = tree

    return answer


# ----------------------------------------------------------------------
def question7():
    answer = {}

    # float
    answer["a, info gain, ID"] = 1.0
    answer["b, info gain, Handedness"] = 0.531004

    # string: "ID" or "Handedness"
    answer["c, which attrib"] = "ID"

    # answer is a float
    answer["d, gain ratio, ID"] = 0.231378
    answer["e, gain ratio, Handedness"] = 0.531004

    # string: one of 'ID' or 'Handedness' based on gain ratio
    # choose the attribute with the largest gain ratio
    answer["f, which attrib"] = "Handedness"

    return answer


# ----------------------------------------------------------------------

if __name__ == "__main__":
    answers = {}
    answers["q1"] = question1()
    answers["q2"] = question2()
    answers["q3"] = question3()
    answers["q4"] = question4()
    answers["q5"] = question5()
    answers["q6"] = question6()
    answers["q7"] = question7()

    u.save_dict("answers.pkl", answers)