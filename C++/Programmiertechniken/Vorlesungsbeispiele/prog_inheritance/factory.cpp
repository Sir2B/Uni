#include <iostream>
#include <string>

using namespace std;

class Document {
public:
  Document(string& s) { name_ = s;}
  virtual void open() = 0;
  virtual void close() = 0;
private:
  string name_;
};


class TextDocument : public Document {
public:
  TextDocument(string& s) : Document(s) {}
  void open() { cout << "TextDocument: open()\n";}
  void close() { cout << "TextDocument: close()\n";}
};

class SpreadSheet : public Document {
public:
  SpreadSheet(string& s) : Document(s) {}
  void open() { cout << "SpreadSheet: open()\n";}
  void close() { cout << "SpreadSheet: close()\n";}
};

class Presentation : public Document {
public:
  Presentation(string& s) : Document(s) {}
  void open() { cout << "Presentation open()\n";}
  void close() { cout << "Presentation close()\n";}
};

class DocumentFactory {
public:
  DocumentFactory() : index_(0) { cout << "DocumentFactory constructor\n";}
  void NewDocument(string& doc_type, string& s) {
    cout << "DocumentFactory: NewDocument()\n";
    docs_[index_] = CreateDocument(doc_type, s);
    docs_[index_]->open();
    index_++;
  }
  virtual Document* CreateDocument(string&, string& ) = 0;
private:
  size_t index_;
  Document *docs_[10];
};

class Project : public DocumentFactory {
public:
  Project() { cout << "Project constructor\n";}
  Document* CreateDocument(string& doc_type, string& s) {
    cout << "Project : CreateDocument()\n";
    if (doc_type == "Text") {
      return new TextDocument(s);
    }
    else if (doc_type == "SpreadSheet") {
      return new SpreadSheet(s);
    }
    else if (doc_type == "Presentation") {
      return new Presentation(s);
    }
    else {
      return nullptr;
    }
  }
};

int main() {
  Project GrantProposal;
  string text_type = "Text";
  string presentation_type = "Presentation";
  string name1 = "foo";
  string name2 = "bar";
  string name3 = "baz";
  GrantProposal.NewDocument(presentation_type, name1);
  GrantProposal.NewDocument(text_type, name2);
  GrantProposal.NewDocument(text_type, name3);
}

