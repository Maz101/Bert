from sklearn.metrics import precision_score, accuracy_score, recall_score
import tensorflow as tf

flags = tf.flags
FLAGS = flags.FLAGS

flags.DEFINE_string("testpath", "None", "testpath dir")
flags.DEFINE_string("testpred", "None", "testpred dir")
testd = []
with open(FLAGS.testpath,'r') as testfile:
    for n in testfile:
        n = n.split('\t')
        testd.append(n[2])
print(len(testd))
    
testpred = []
with open(FLAGS.testpred,'r') as testfile:
    for n in testfile:
        n = n.split('\t')
        maxvalue = max(n)
        indexmx = n.index(maxvalue) + 1
        testpred.append(indexmx)
        
print(len(testpred))
    
ac = accuracy_score(testd, testpred)
pc = precision_score(testd, testpred)
rc = recall_score(testd, testpred)
    
print("** Accuracy", ac)
print("** Precision",pc)
print("** Recall", rc)
