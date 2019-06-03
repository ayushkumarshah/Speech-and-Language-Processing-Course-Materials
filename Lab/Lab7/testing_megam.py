
import nltk


nltk.config_megam('C:\\OCaml64\\home\\ayush\\megam_0.92\\megam.exe')
trainer = lambda x: nltk.MaxentClassifier.train(x, 'megam')
print("Hello")
# nltk.classify.rte_classifier(trainer) 

