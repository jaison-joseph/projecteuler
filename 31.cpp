#include<memory>
#include <iostream>
using namespace std;

#define print(x) cout << endl << x
#define show(x) cout << endl << #x << " : " << x
#define label_show(label,val) cout << endl << label << " : " << val

struct Node{
	int num;
	shared_ptr<shared_ptr<Node>> children;
	Node(int num_) :
		num(num_)
	{ }
	Node(void) :
		num(1)
	{ }
	int getNum() {return num;}
};

class Tree {
	Node parent;
	public:

		Tree() {
			print("tree created");
		}

		Tree(int num) : parent(num)
		{
			print("int tree created");
		}

		void showw() {
			label_show("Parent number", parent.getNum());
		}

};

int main() {
	Tree tree(2);
}
