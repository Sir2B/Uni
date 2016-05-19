#include <iostream>
#include <vector>
#include <cstdlib>

using namespace std;

class Shape
{
public:
    Shape() {};
    virtual void setColor()
    {
        cout << " Shape::setColor() called "<< endl;
    }
    virtual void Draw()
    {
        cout << " Shape::Draw() called "<< endl;
    }
    //..
};
class Rectangle : public Shape
{
    virtual void Draw()
public:
    {
        cout << " Rectangle::Draw() called "<< endl;
    }
};
class Oval  : public Shape
{
public:
    void Draw()
    {
        cout << " Oval::Draw() called "<< endl;
    }
};
class RoundRect : public Shape
{
public:
    void Draw()
    {
        cout << " RoundRect::Draw() called "<< endl;
    }
};
int main ()
{
    vector<Shape*> vecshape;  // vector with base-class pointers

    // add some concrete shapes
    vecshape.push_back( new Rectangle());
    vecshape.push_back( new Oval());
    vecshape.push_back( new Rectangle());
    vecshape.push_back( new RoundRect());
    vecshape.push_back( new Oval());
    vecshape.push_back( new Oval());

    for ( int i=0; i<vecshape.size(); i++ )
    {
        vecshape[i]->setColor( );
        vecshape[i]->Draw( );
    }
}
