# HotDog-Nothotdog

"What would you say if I told you there is a app on the market that tell you if you have a hotdog or not a hotdog. 


![Alt text](/687474703a2f2f696d672e796f75747562652e636f6d2f76692f41436d79647446445447732f302e6a7067.jpg?raw=true "Optional Title")
![Alt text](/cat.jpg?raw=true "Optional Title")

# Collect the data
  <h3> Training Data</h3>
  
  1- HotDogs images
  
  2- NotHotdogs Images(Random images)
  
  
We can use some food image datasets Like
    
      http://mmspg.epfl.ch/food-image-datasets
      
      https://www.vision.ee.ethz.ch/datasets_extra/food-101/
      
      or use imagenet

# How to train it?
  Convolutional Neural Networks (ConvNets or CNNs) are a category of Neural Networks that have proven very effective in areas such as image recognition and classification. ConvNets have been successful in identifying faces, objects and traffic signs apart from powering vision in robots and self driving cars.    



    ![Alt text](/CNN.jpg?raw=true "Optional Title")

Model, That I've used!!
![Alt text](/model.png?raw=true "Optional Title")
 
 You can use this model too 
 <table>
<thead>
<tr>
<th align="center">Layer</th>
<th align="center">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center">Input</td>
<td align="center">128x128x1 Gray scale image</td>
</tr>
<tr>
<td align="center">Convolution 8x8</td>
<td align="center">4x4 subsampling</td>
</tr>
<tr>
<td align="center">ELU</td>
<td align="center"></td>
</tr>
<tr>
<td align="center"></td>
<td align="center"></td>
</tr>
<tr>
<td align="center">Convolution 5x5</td>
<td align="center">2x2 subsampling</td>
</tr>
<tr>
<td align="center">ELU</td>
<td align="center"></td>
</tr>
<tr>
<td align="center"></td>
<td align="center"></td>
</tr>
<tr>
<td align="center">Convolution 5x5</td>
<td align="center">2x2 subsampling</td>
</tr>
<tr>
<td align="center">Flatten</td>
<td align="center"></td>
</tr>
<tr>
<td align="center">Dropout</td>
<td align="center">.2 dropout probability</td>
</tr>
<tr>
<td align="center">ELU</td>
<td align="center"></td>
</tr>
<tr>
<td align="center"></td>
<td align="center"></td>
</tr>
<tr>
<td align="center">Fully connected</td>
<td align="center">output 512</td>
</tr>
<tr>
<td align="center">Dropout</td>
<td align="center">.5 dropout probability</td>
</tr>
<tr>
<td align="center">ELU</td>
<td align="center"></td>
</tr>
<tr>
<td align="center"></td>
<td align="center"></td>
</tr>
<tr>
<td align="center">Fully connected</td>
<td align="center">output 2</td>
</tr>
<tr>
<td align="center">Softmax</td>
<td align="center">output 2</td>
</tr></tbody></table>

(use model.h5)
