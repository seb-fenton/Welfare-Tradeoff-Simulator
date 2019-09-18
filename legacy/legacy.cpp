#include <iostream>
#include <vector>

using namespace std;
struct actionMemory{
  int action;
  int id;
};

struct statistics{
  int energy = 0;
  int pop = 0;
};

class Morph {
public:
  //constructor
  Morph(int _id, int _colour, int _energy): id(_id), colour(_colour), energy(_energy){}

  //basic functions - here to ensure data protection
  int getColour() {
    return colour;
  }
  int getId() {
    return id;
  }
  int getEnergy() {
    return energy;
  }

  //remembers the action of a
  void storeAction(int actor, int action){
    actionMemory temp;
    temp.action = action;
    temp.id = actor;
    memory.push_back(temp);
  }

  int recallAction(int target_id){
    if(memory.size() > 0){
      for(int i = memory.size()-1; i >= 0; i--){
        if(memory[i].id == target_id){return memory[i].action;}
      }
    }
    return 2;
  }

  int modifyEnergy(int modifier){
    energy += modifier;
    return energy;
  }

  bool randomChoice(){
    int r = rand() % 2;
    if(r == 1) return true;
    else return false;
  }

  bool makeChoice(int target, int target_colour){
    //here we define the rules for species choice behaviour. change this area
    int action = 2;
    switch(colour){
      case 0:   return randomChoice();
                break;
      case 1:   {
                action = recallAction(target); // will receive 0 - thisish, 1 - thisless, 2 - no memory
                if(action == 0) return false;
                else if(action == 1) return true;
                else if(action == 2) return randomChoice();
                } break;
      case 2:   return true;
                break;
      case 3:   return false;
                break;
      case 4:   {
                if(target_colour == colour){return true;}
                else return false;
                } break;
    }
  }

private:
  int colour;
  int id;
  int energy;
  std::vector<actionMemory> memory;
};


void popPrint(std::vector<Morph> population){
  for(int i = 0; i < population.size(); i++){
    std::cout << i << ": E" << population[i].getEnergy() << " C" << population[i].getColour() << std::endl;
  }
}

void popStats(std::vector<Morph> population){
  statistics colourStats[5];
  int totalEnergy = 0;
  for(int i = 0; i < population.size(); i++){
    int n = population[i].getColour();
    switch(n){
      case 0: {
              colourStats[0].pop++;
              colourStats[0].energy += population[i].getEnergy();
              totalEnergy += population[i].getEnergy();
              } break;
      case 1: {
              colourStats[1].pop++;
              colourStats[1].energy += population[i].getEnergy();
              totalEnergy += population[i].getEnergy();
              } break;
      case 2: {
              colourStats[2].pop++;
              colourStats[2].energy += population[i].getEnergy();
              totalEnergy += population[i].getEnergy();
              } break;
      case 3: {
              colourStats[3].pop++;
              colourStats[3].energy += population[i].getEnergy();
              totalEnergy += population[i].getEnergy();
              } break;
      case 4: {
              colourStats[4].pop++;
              colourStats[4].energy += population[i].getEnergy();
              totalEnergy += population[i].getEnergy();
              } break;
    }
    std::cout << "n: " << n << std::endl;
  }
  std::cout << "\033[1;36mBlue Population: \033[0m" << colourStats[0].pop << std::endl;
  std::cout << "\033[1;36mBlue Energy: \033[0m" << colourStats[0].energy << std::endl;
  std::cout << "\033[1;32mGreen Population: \033[0m" << colourStats[1].pop << std::endl;
  std::cout << "\033[1;32mGreen Energy: \033[0m" << colourStats[1].energy << std::endl;
  std::cout << "\033[1;31mRed Population: \033[0m" << colourStats[2].pop << std::endl;
  std::cout << "\033[1;31mRed Energy: \033[0m" << colourStats[2].energy << std::endl;
  std::cout << "\033[1;35mPink Population: \033[0m" << colourStats[3].pop << std::endl;
  std::cout << "\033[1;35mPink Energy: \033[0m" << colourStats[3].energy << std::endl;
  std::cout << "\033[1;33mYellow Population: \033[0m" << colourStats[4].pop << std::endl;
  std::cout << "\033[1;33mYellow Energy: \033[0m" << colourStats[4].energy << std::endl;
}


int main(){
  //here we define the rules for species memory behaviour
  std::cout << "Input numbers for each species:\n";

  std::cout << "Random Blue: ";
  int bluePop;
  std::cin >> bluePop;

  std::cout << "Reciprocal Green: ";
  int greenPop;
  std::cin >> greenPop;

  std::cout << "Selfish Red: ";
  int redPop;
  std::cin >> redPop;

  std::cout << "Wholesome Pink: ";
  int pinkPop;
  std::cin >> pinkPop;

  std::cout << "Kinship Yellow: ";
  int yellowPop;
  std::cin >> yellowPop;

  int uniqueId = 0;
  std::vector<Morph> population;

  for(int i = 0; i < bluePop; i++){
    Morph temp(uniqueId, 0, 6);
    population.push_back(temp);
    uniqueId++;
   }

   for(int i = 0; i < greenPop; i++){
     Morph temp(uniqueId, 1, 6);
     population.push_back(temp);
     uniqueId++;
    }

   for(int i = 0; i < redPop; i++){
      Morph temp(uniqueId, 2, 6);
      population.push_back(temp);
      uniqueId++;
    }

    for(int i = 0; i < pinkPop; i++){
       Morph temp(uniqueId, 3, 6);
       population.push_back(temp);
       uniqueId++;
    }

    for(int i = 0; i < yellowPop; i++){
      Morph temp(uniqueId, 4, 6);
      population.push_back(temp);
      uniqueId++;
     }

     popPrint(population);

     int turns;
     std::cout << "Number of turns: ";
     std::cin >> turns;
     std::cout << "Game beginning..." << std::endl;

     while(turns > 0){
       std::random_shuffle(population.begin(), population.end()-1);
       int size = population.size();

       int i = 0;

       while(i < size){

         bool result = population[i].makeChoice(population[i+1].getId(), population[i+1].getColour());
          if(result == true){
            int temp = population[i+1].modifyEnergy(6);
            if(population[i+1].getEnergy()>=12){
              population[i+1].modifyEnergy(-6);
              Morph newMorph(uniqueId, population[i+1].getColour(), 6);
              population.push_back(newMorph);
              uniqueId++;
            }
            if(population[i+1].getColour()==1){
              population[i+1].storeAction(population[i].getId(), 1);
            }
          }
          else{
            population[i].modifyEnergy(4);
            if(population[i].getEnergy()>=12){
              population[i].modifyEnergy(-6);
              Morph newMorph(uniqueId, population[i].getColour(), 6);
              population.push_back(newMorph);
              uniqueId++;
            }
            if(population[i+1].getColour()==1){
              population[i+1].storeAction(population[i].getId(), 0);
            }
          }
          i+=2;
       }

       for(int i = 0; i < size; i++){
         int temp = population[i].modifyEnergy(-1); //tax
         if(temp <= 0) {
           std::cout << "i: " << i << std::endl;
           std::cout << "popsize: " << population.size() << std::endl;
           population.erase(population.begin()+i);
           std::cout << "managed" << std::endl;
         }
       }

       turns--;
       std::cout << "Turns: " << turns << std::endl;
       popPrint(population);
     }

     std::cout << "Game over, here are the results: \n";
     popStats(population);
}