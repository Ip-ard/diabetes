import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn import tree
import streamlit as st


from web_functions import train_model

def app(dataset, x, y):

    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.title("Visualisasi Prediksi Diabetes")

    # if st.checkbox("Plot Confusion Matrix"):
    #     model, score = train_model(x,y)
    #     plt.figure(1)
    #     confusion_matrix(model, x, y, values_format='d')
    #     st.pyplot()

    if st.checkbox("Decision Tree"):
        model, score = train_model(x,y)
        dot_data = tree.export_graphviz(
            decision_tree=model, max_depth=3, out_file=None, filled=True, rounded=True,
            feature_names=x.columns, class_names=['nockd', 'ckd']
        )

        st.graphviz_chart(dot_data)
