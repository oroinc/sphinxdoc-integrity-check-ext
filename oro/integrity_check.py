import hashlib
import sphinx

from docutils import nodes
from docutils.parsers.rst import Directive


class OroIntegrityCheck(Directive):
    """
    Class that checks hash of directive's content and compare it to the hash specified in document
    """
    required_arguments = 1
    has_content = True

    def run(self):
        document_hash = self.arguments[0]

        node = nodes.container()
        node.document = self.state.document
        self.state.nested_parse(self.content, self.content_offset, node)

        node_hash = self.calculate_hash(node.astext())

        if document_hash != node_hash:
            message = 'Node hashes are different. "%s" expected, but "%s" given' % (node_hash, document_hash)
            self.state.document.reporter.warning(message, line=self.lineno)
            warning_node = self.create_warning_node()
            return [warning_node, node]

        return [node]

    def calculate_hash(self, content):
        """
        Calculate hash of content
        :param content: str
        :return: str
        """

        sha1 = hashlib.sha1()
        sha1.update(content.encode('utf-8'))
        return sha1.hexdigest()

    def create_warning_node(self):
        """
        Method creates warning node when hash of directive content
        is not match to content integrity hash in the rst document
        """

        item = nodes.paragraph()
        item.append(nodes.warning('', nodes.inline(text="This code example can be not actual for this version")))

        return item


def setup(app):
    app.add_directive('oro_integrity_check', OroIntegrityCheck)
    return {'version': sphinx.__display_version__, 'parallel_read_safe': True}
