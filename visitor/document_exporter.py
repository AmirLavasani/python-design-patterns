# Step 1: Define the Visitor Interface
class Exporter:
    def export_paragraph(self, paragraph):
        pass

    def export_heading(self, heading):
        pass

    def export_image(self, image):
        pass


# Step 2: Implement Concrete Visitors
class HTMLExporter(Exporter):
    def export_paragraph(self, paragraph):
        return f"<p>{paragraph.content}</p>"

    def export_heading(self, heading):
        return f"<h{heading.level}>{heading.text}</h{heading.level}>"

    def export_image(self, image):
        return f'<img src="{image.source}" alt="{image.alt}">'


class PDFExporter(Exporter):
    def export_paragraph(self, paragraph):
        return f"PDF Paragraph: {paragraph.content}"

    def export_heading(self, heading):
        return f"PDF Heading ({heading.level}): {heading.text}"

    def export_image(self, image):
        return f'PDF Image: {image.alt}'


# Step 3: Define Element Interface
class Element:
    def accept(self, visitor):
        pass


# Step 4: Implement Concrete Elements
class Paragraph(Element):
    def __init__(self, content):
        self.content = content

    def accept(self, visitor):
        return visitor.export_paragraph(self)

class Heading(Element):
    def __init__(self, level, text):
        self.level = level
        self.text = text

    def accept(self, visitor):
        return visitor.export_heading(self)

class Image(Element):
    def __init__(self, source, alt):
        self.source = source
        self.alt = alt

    def accept(self, visitor):
        return visitor.export_image(self)


# Step 5: Client Code
class Document:
    def __init__(self, elements):
        self.elements = elements

    def accept(self, visitor):
        result = []
        for element in self.elements:
            result.append(element.accept(visitor))
        return result


# Usage
html_exporter = HTMLExporter()
pdf_exporter = PDFExporter()

document = Document([
    Paragraph("This is a paragraph."),
    Heading(1, "Main Heading"),
    Image("image.jpg", "A beautiful image")
])

# Export to HTML
html_result = document.accept(html_exporter)
print("HTML Export:")
print('\n'.join(html_result))
print("\n")

# Export to PDF
pdf_result = document.accept(pdf_exporter)
print("PDF Export:")
print('\n'.join(pdf_result))