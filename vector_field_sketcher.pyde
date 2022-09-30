out = 300
w = out/2
class points:
    def __init__(self):
        self.point_array=[]
        self.density = 10
        self.zoom_factor = 2
        #for i in range(-w/2,w/2,self.density):
        #    for j in range(-w/2,w/2,self.density):
        #        self.point_array.append([i,j])
    def set_zoom(self,factor):
        self.zoom_factor = factor           
    def show(self):
        for i in self.point_array:
            stroke(i[2],i[2],255-i[2])
            strokeWeight(2)
            if (dist(0,0,i[0],i[1])<=2*out):
                point(i[0],i[1])
    
    def update_positions(self):
        out_indexes = []
        for i in range(len(self.point_array)):
            if self.point_array[i][0]<-out/2 or self.point_array[i][0]>out/2 or self.point_array[i][1]>out/2 or self.point_array[i][1]<-out/2:
                out_indexes.append(i)
        for i in range(len(self.point_array),0,-1):
            if (i in out_indexes):
                self.point_array.pop(i)
        for i in self.point_array:
            x = float(i[0]/(w/self.zoom_factor))
            y = float(i[1]/(w/self.zoom_factor))
            i[0] += -y+x
            i[1] += x
            #update  vectors
        #chck if they are out of screen
        
        for j in self.point_array:
            distance = sqrt(j[0]*j[0]+j[1]*j[1])
            
            normalised_distance = map(distance,0,0.8*out,0,255)
            j[2]=normalised_distance
    def add_vectors(self):
        for i in range(-w,w,self.density):
            #print(multiplier)
            #self.point_array.append([(multiplier)*(w/2),(multiplier)*(w/2)])
            self.point_array.append([i,i,0])
            self.point_array.append([i,-i,0])
            self.point_array.append([i,0,0])
            self.point_array.append([0,i,0])
            #self.point_array.append([100+w-i,i,0])
            #self.point_array.append([70+w-i,i,0])
            #self.point_array.append([50+w-i,i,0])
            #self.point_array.append([40+w-i,i,0])
            #self.point_array.append([30+w-i,i,0])
            #self.point_array.append([w-50-i,i,0])
            #self.point_array.append([i,0,0])
            #self.point_array.append([0,i,0])
            #self.point_array.append([-(multiplier)*(w/2),-(multiplier)*(w/2)])
    def return_points(self):
        return(len(self.point_array))

    
obj = points()
zoom_value = 2
def setup():
    size(500,500)
    obj.set_zoom(zoom_value)
def draw():
    global zoom_value
    m = millis()
    background(0)
    translate(width/2,height/2)
    
    
    if (m%2==0 and obj.return_points()<=10000):
        obj.add_vectors()
    stroke(255)
    text(str(obj.return_points()),0,-200)
    text(str(zoom_value),200,-200)
    obj.update_positions()
    #zoom_value += -0.005
    obj.set_zoom(zoom_value)
    obj.show()
    
    
                
